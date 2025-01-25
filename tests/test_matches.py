def test_create_match(client, auth_token):
    # Create target user
    target = User(
        name="Match Target",
        email="target@example.com",
        seat_section="A1",
        attendance_date="2025-01-01"
    )
    db.session.add(target)
    db.session.commit()
    
    response = client.post(
        f'/api/matches/match/{target.id}',
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    
    assert response.status_code == 200
    assert response.json['status'] == 'pending'
