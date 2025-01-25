from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from ..models import User, db
from ..utils.email import send_magic_link
from ..utils.security import hash_password, verify_password

bp = Blueprint('auth', __name__, url_prefix='/api/auth')
auth_bp = Blueprint('auth', __name__)
@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Validate required fields
    required_fields = ['name', 'attendance_date', 'seat_section']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
        
    # Validate contact information
    if not data.get('email') and not data.get('mobile'):
        return jsonify({'error': 'Either email or mobile is required'}), 400
    
    # Create new user
    user = User(
        name=data['name'],
        email=data.get('email'),
        mobile=data.get('mobile'),
        attendance_date=data['attendance_date'],
        seat_section=data['seat_section']
    )
    
    db.session.add(user)
    db.session.commit()
    #token = create_access_token(identity=user.id)
    #return jsonify({'token': token}), 201
    # Send magic link if email provided
    if user.email:
        send_magic_link(user.email)
    
    return jsonify({'message': 'Registration successful'}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    # Handle magic link token
    if 'token' in data:
        # Verify magic link token
        user = verify_magic_link_token(data['token'])
        if user:
            access_token = create_access_token(identity=user.id)
            return jsonify({'access_token': access_token}), 200
    
    return jsonify({'error': 'Invalid login attempt'}), 401


auth_bp = Blueprint('auth', __name__)


from datetime import datetime, timedelta
import jwt
from flask import current_app

def verify_magic_link_token(token):
    try:
        # Decode and verify the magic link token
        payload = jwt.decode(
            token,
            current_app.config['SECRET_KEY'],
            algorithms=['HS256']
        )
        
        # Check if token is expired (typically 15 minutes)
        if datetime.fromtimestamp(payload['exp']) < datetime.utcnow():
            return None
            
        return payload['email']
        
    except jwt.InvalidTokenError:
        return None

