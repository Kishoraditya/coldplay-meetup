from datetime import datetime
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True)
    mobile = db.Column(db.String(20), unique=True)
    seat_section = db.Column(db.String(50), nullable=False)
    attendance_date = db.Column(db.DateTime, nullable=False)
    profile_data = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    matches = db.relationship('Match', backref='user', lazy=True)

    # Optional fields
    photos = db.Column(db.JSON)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(20))
    sexuality = db.Column(db.String(50))
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    
    # Additional profile fields
    extra_tickets = db.Column(db.Boolean, default=False)
    traveling_with = db.Column(db.String(50))
    job_role = db.Column(db.String(100))
    company = db.Column(db.String(100))
    purpose = db.Column(db.String(50), nullable=False)
    
    # Social links
    social_links = db.Column(db.JSON)
    
    # Preferences and interests
    top_songs = db.Column(db.JSON)
    top_bands = db.Column(db.JSON)
    top_movies = db.Column(db.JSON)
    top_books = db.Column(db.JSON)
    
    # Personal details
    workout = db.Column(db.Boolean)
    drinks = db.Column(db.Boolean)
    smokes = db.Column(db.Boolean)
    drugs = db.Column(db.Boolean)
    specially_abled = db.Column(db.Boolean)
    marital_status = db.Column(db.String(20))
    has_kids = db.Column(db.Boolean)
    wants_kids = db.Column(db.Boolean)
    
    scam_meter = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    matched_with_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AuditEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    action = db.Column(db.String(50))
    details = db.Column(db.Text)
