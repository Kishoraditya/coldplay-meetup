from scripts.monitoring.memory_profiler import profile
from app.backend.models import User, Match

@profile
def analyze_memory_usage():
    # Create large dataset
    users = [create_test_user(i) for i in range(10000)]
    
    # Test memory usage during operations
    for i in range(100):
        # Simulate concurrent operations
        view_profiles(users[i])
        create_matches(users[i], users)
        update_user_profile(users[i])

def create_test_user(i):
    return User(
        name=f"User_{i}",
        email=f"user_{i}@test.com",
        seat_section=f"Section_{i%10}",
        attendance_date="2025-01-01"
    )

@profile
def view_profiles(user):
    # Simulate profile viewing
    profiles = User.query.filter(
        User.seat_section == user.seat_section,
        User.id != user.id
    ).limit(50).all()
    return [p.to_dict() for p in profiles]

import memory_profiler
from app.backend.models import User, Match
from app.backend.routes.matches import create_matches, update_user_profile

@memory_profiler.profile
def profile_matching():
    users = User.query.all()
    create_matches(users)
    update_user_profile(users[0])

