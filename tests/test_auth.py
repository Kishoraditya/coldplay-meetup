def test_registration(client):
    response = client.post('/api/auth/register', json={
        'name': 'New User',
        'email': 'new@example.com',
        'seat_section': 'B2',
        'attendance_date': '2025-01-01'
    })
    
    assert response.status_code == 201
    assert 'token' in response.json

def test_invalid_registration(client):
    response = client.post('/api/auth/register', json={
        'name': 'New User'
    })
    
    assert response.status_code == 400
