import pytest
from app import create_app
from app.models import db, User, Match

@pytest.fixture
def app():
    app = create_app('testing')
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_token(client):
    user = User(
        name="Test User",
        email="test@example.com",
        seat_section="A1",
        attendance_date="2025-01-01"
    )
    db.session.add(user)
    db.session.commit()
    
    response = client.post('/api/auth/login', json={
        'email': 'test@example.com'
    })
    return response.json['token']
