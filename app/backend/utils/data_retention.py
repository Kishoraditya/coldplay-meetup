from ..models import db
from ..utils.s3 import delete_file
import logging

class DataRetention:
    @staticmethod
    def remove_user_data(user_id):
        try:
            user = User.query.get(user_id)
            if not user:
                return
            
            # Delete profile photos
            if user.photos:
                for photo in user.photos:
                    delete_file(photo)
            
            # Remove sensitive information
            user.email = None
            user.mobile = None
            user.social_links = None
            
            # Mark as deleted but keep basic stats
            user.is_deleted = True
            user.name = "Deleted User"
            
            db.session.commit()
            
            logging.info(f"Successfully removed data for user {user_id}")
            
        except Exception as e:
            logging.error(f"Error removing data for user {user_id}: {str(e)}")
            raise
