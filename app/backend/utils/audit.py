from ..models import db
import logging

class AuditLog:
    @staticmethod
    def log_deletion(user_id, reason):
        logging.info(f"Data deletion for user {user_id}. Reason: {reason}")
        
        # Store in audit table
        audit = AuditEntry(
            user_id=user_id,
            action="deletion",
            reason=reason,
            ip_address=request.remote_addr
        )
        db.session.add(audit)
        db.session.commit()
    
    @staticmethod
    def export_audit_log(start_date, end_date):
        entries = AuditEntry.query.filter(
            AuditEntry.created_at.between(start_date, end_date)
        ).all()
        
        return [{
            'user_id': entry.user_id,
            'action': entry.action,
            'reason': entry.reason,
            'timestamp': entry.created_at.isoformat()
        } for entry in entries]
        
from flask import request
from ..models import AuditEntry, db

def log_audit_event(action, details=None):
    entry = AuditEntry(
        user_id=request.user_id if hasattr(request, 'user_id') else None,
        action=action,
        details=details
    )
    db.session.add(entry)
    db.session.commit()
