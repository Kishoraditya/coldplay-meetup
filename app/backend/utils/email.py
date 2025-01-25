import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_magic_link(email, token):
    # Using Gmail SMTP (free)
    sender = "your-app@gmail.com"
    msg = MIMEMultipart()
    msg['Subject'] = "Your Coldplay Meetup Login Link"
    msg['From'] = sender
    msg['To'] = email
    
    link = f"https://yourdomain.tk/verify/{token}"
    html = f"""
    <h2>Welcome to Coldplay Meetup!</h2>
    <p>Click <a href="{link}">here</a> to login.</p>
    """
    
    msg.attach(MIMEText(html, 'html'))
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, "app-specific-password")
        server.send_message(msg)
