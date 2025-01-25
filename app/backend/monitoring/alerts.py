from flask import Blueprint, request, jsonify
from .notifications import send_notification

alerts_bp = Blueprint('alerts', __name__)

@alerts_bp.route('/alert', methods=['POST'])
def handle_alert():
    alert_data = request.json
    
    # Process different alert types
    if alert_data['alertname'] == 'HighErrorRate':
        send_notification(
            'High error rate detected',
            f"Error rate exceeded threshold: {alert_data['value']}"
        )
    elif alert_data['alertname'] == 'ServerLoad':
        send_notification(
            'High server load',
            f"Server load at {alert_data['value']}%"
        )
    
    return jsonify({'status': 'processed'})
