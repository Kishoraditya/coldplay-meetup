from datetime import datetime, timedelta
import boto3
import logging

class CostOptimizer:
    def __init__(self):
        self.ec2 = boto3.client('ec2')
        self.cloudwatch = boto3.client('cloudwatch')
    
    def optimize_resources(self):
        self.cleanup_unused_volumes()
        self.optimize_instance_types()
        self.schedule_scaling()
    
    def cleanup_unused_volumes(self):
        volumes = self.ec2.describe_volumes(
            Filters=[{'Name': 'status', 'Values': ['available']}]
        )
        for volume in volumes['Volumes']:
            if self.is_unused_for_days(volume['CreateTime'], 7):
                self.ec2.delete_volume(VolumeId=volume['VolumeId'])
                logging.info(f"Deleted unused volume: {volume['VolumeId']}")
    
    def optimize_instance_types(self):
        instances = self.ec2.describe_instances()
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                metrics = self.get_instance_metrics(instance['InstanceId'])
                if metrics['cpu_utilization'] < 20:
                    self.recommend_downsizing(instance)
