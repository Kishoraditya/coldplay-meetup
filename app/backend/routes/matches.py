from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import User, Match, db
from ..utils.redis_client import redis_client
from .matching import calculate_compatibility, calculate_reveal_time, schedule_contact_reveal
bp = Blueprint('matches', __name__, url_prefix='/api/matches')

@bp.route('/like/<int:profile_id>', methods=['POST'])
@jwt_required()
def like_profile(profile_id):
    user_id = get_jwt_identity()
    
    # Check if users are in same section
    user = User.query.get_or_404(user_id)
    target = User.query.get_or_404(profile_id)
    
    if user.seat_section != target.seat_section:
        return jsonify({'error': 'Cannot match with users in different sections'}), 400
    
    # Create or update match
    match = Match(
        user_id=user_id,
        matched_user_id=profile_id,
        status='pending'
    )
    
    # Check for mutual match
    existing_match = Match.query.filter_by(
        user_id=profile_id,
        matched_user_id=user_id,
        status='pending'
    ).first()
    
    if existing_match:
        # It's a match!
        existing_match.status = 'matched'
        match.status = 'matched'
        
        # Schedule contact info reveal
        reveal_time = calculate_reveal_time(user.attendance_date)
        schedule_contact_reveal(user_id, profile_id, reveal_time)
    
    db.session.add(match)
    db.session.commit()
    
    return jsonify({'status': match.status}), 200


matches_bp = Blueprint('matches', __name__)
@matches_bp.route('/match/<int:target_id>', methods=['POST'])
@jwt_required()
def create_match(target_id):
    user_id = get_jwt_identity()
    
    # Check if users are in same section
    user = User.query.get_or_404(user_id)
    target = User.query.get_or_404(target_id)
    
    if user.seat_section != target.seat_section:
        return jsonify({'error': 'Users must be in same section'}), 400
    
    # Create match
    match = Match(user_id=user_id, matched_with_id=target_id)
    db.session.add(match)
    
    # Check for mutual match
    mutual = Match.query.filter_by(
        user_id=target_id, 
        matched_with_id=user_id
    ).first()
    
    if mutual:
        match.status = 'matched'
        mutual.status = 'matched'
        redis_client.set(f'match:{user_id}:{target_id}', 'matched')
    
    db.session.commit()
    return jsonify({'status': match.status})
