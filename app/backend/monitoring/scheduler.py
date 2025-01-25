from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from ..models import User, Match, db

class CleanupScheduler:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.setup_jobs()

    def setup_jobs(self):
        # Run cleanup every day at 3 AM
        self.scheduler.add_job(
            self.cleanup_old_data,
            'cron',
            hour=3
        )
        
        # Check expired matches every hour
        self.scheduler.add_job(
            self.cleanup_expired_matches,
            'interval',
            hours=1
        )

    def cleanup_old_data(self):
        cutoff_date = datetime.utcnow() - timedelta(hours=24)
        
        # Delete users and their matches after event
        expired_users = User.query.filter(
            User.attendance_date < cutoff_date
        ).all()
        
        for user in expired_users:
            Match.query.filter(
                (Match.user_id == user.id) |
                (Match.matched_with_id == user.id)
            ).delete()
            db.session.delete(user)
        
        db.session.commit()

    def cleanup_expired_matches(self):
        cutoff = datetime.utcnow() - timedelta(hours=1)
        
        # Delete unmatched requests after 1 hour
        Match.query.filter(
            Match.status == 'pending',
            Match.created_at < cutoff
        ).delete()
        
        db.session.commit()

    def start(self):
        self.scheduler.start()
