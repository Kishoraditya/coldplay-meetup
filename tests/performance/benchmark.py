import cProfile
import pstats
from app import create_app
from app.models import User, Match

def profile_matching_algorithm():
    profiler = cProfile.Profile()
    app = create_app('testing')
    
    with app.app_context():
        # Create test data
        users = [
            User(
                name=f"User_{i}",
                seat_section=f"Section_{i%5}",
                attendance_date="2025-01-01"
            ) for i in range(1000)
        ]
        
        # Profile the matching process
        profiler.enable()
        for user in users[:100]:
            find_matches(user, users)
        profiler.disable()
        
        # Print results
        stats = pstats.Stats(profiler)
        stats.sort_stats('cumulative')
        stats.print_stats(20)

def find_matches(user, all_users):
    return [
        u for u in all_users
        if u.id != user.id
        and u.seat_section == user.seat_section
        and calculate_compatibility(user, u) > 0.7
    ]
