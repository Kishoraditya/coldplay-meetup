from datetime import datetime
import redis
import json

class Analytics:
    def __init__(self):
        self.redis_client = redis.Redis()
        
    def track_event(self, event_name, user_id=None, metadata={}):
        event = {
            'timestamp': datetime.utcnow().isoformat(),
            'event': event_name,
            'user_id': user_id,
            'metadata': metadata
        }
        self.redis_client.lpush('analytics', json.dumps(event))
        
    def get_daily_stats(self):
        return {
            'new_users': self.count_daily_events('user_registered'),
            'matches_made': self.count_daily_events('match_created'),
            'active_users': self.count_unique_users()
        }
