from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import User, db
from ..utils.s3 import upload_photo

bp = Blueprint('profiles', __name__, url_prefix='/api/profiles')
profiles_bp = Blueprint('profiles', __name__)
@bp.route('/me', methods=['GET'])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())

@bp.route('/me', methods=['PUT'])
@jwt_required()
def update_profile():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    
    # Update optional fields
    optional_fields = [
        'photos', 'age', 'gender', 'sexuality', 'height', 'weight',
        'extra_tickets', 'traveling_with', 'job_role', 'company',
        'purpose', 'social_links', 'top_songs', 'top_bands',
        'top_movies', 'top_books', 'workout', 'drinks', 'smokes',
        'drugs', 'specially_abled', 'marital_status', 'has_kids',
        'wants_kids', 'scam_meter'
    ]
    
    for field in optional_fields:
        if field in data:
            setattr(user, field, data[field])
    
    db.session.commit()
    return jsonify(user.to_dict())

@bp.route('/section/<section>', methods=['GET'])
@jwt_required()
def get_section_profiles(section):
    current_user = User.query.get(get_jwt_identity())
    
    # Get profiles in same section, excluding current user
    profiles = User.query.filter(
        User.seat_section == section,
        User.id != current_user.id
    ).all()
    
    return jsonify([p.to_dict() for p in profiles])




@profiles_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())

@profiles_bp.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    
    for key, value in data.items():
        if hasattr(user, key):
            setattr(user, key, value)
    
    db.session.commit()
    return jsonify(user.to_dict())

