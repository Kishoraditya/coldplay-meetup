import os
import subprocess
from pathlib import Path

class SecurityHardening:
    def __init__(self):
        self.security_rules = {
            'file_permissions': 0o644,
            'directory_permissions': 0o755,
            'sensitive_files': ['.env', 'secrets.yml']
        }

    def harden_system(self):
        self.update_file_permissions()
        self.configure_firewall()
        self.setup_fail2ban()
        self.enable_security_headers()
        
    def configure_firewall(self):
        rules = [
            "ufw default deny incoming",
            "ufw default allow outgoing",
            "ufw allow ssh",
            "ufw allow http",
            "ufw allow https",
            "ufw enable"
        ]
        for rule in rules:
            subprocess.run(rule.split())
