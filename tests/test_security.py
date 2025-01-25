def test_rate_limiting(client):
    # Make 61 requests (limit is 60)
    for _ in range(61):
        response = client.get('/api/profiles')
    
    assert response.status_code == 429

def test_csrf_protection(client, auth_token):
    response = client.post(
        '/api/profiles/me',
        headers={'Authorization': f'Bearer {auth_token}'}
        # Missing CSRF token
    )
    
    assert response.status_code == 403
