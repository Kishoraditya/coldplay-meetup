def test_update_profile(client, auth_token):
    response = client.put(
        '/api/profiles/me',
        headers={'Authorization': f'Bearer {auth_token}'},
        json={
            'age': 25,
            'bio': 'Test bio',
            'interests': ['music', 'travel']
        }
    )
    
    assert response.status_code == 200
    assert response.json['age'] == 25
