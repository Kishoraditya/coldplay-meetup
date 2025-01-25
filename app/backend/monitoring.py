import logging
from datetime import datetime

class FreeMonitoring:
    def __init__(self):
        logging.basicConfig(
            filename='app.log',
            level=logging.INFO,
            format='%(asctime)s %(levelname)s: %(message)s'
        )
    
    def log_metric(self, metric_name, value):
        logging.info(f"{metric_name}: {value}")
