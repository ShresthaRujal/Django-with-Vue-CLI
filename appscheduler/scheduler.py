from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from app import models
from app.serializers import UserProfileSerialzer


def start():
    '''start scheduling job'''
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_signupEmail, 'interval', minutes=1)
    scheduler.start()

def send_signupEmail():
    queryset = list(models.UserProfile.objects.exclude(is_email_sent=True))
    to_email = []
    for e in queryset:
        to_email.append(e.email)
    subject = "Thank you"
    from_email ='donotreply@gmail.com'
    signup_message = """Welcome to blablalba """
    send_mail(subject=subject,
    from_email=from_email,
    recipient_list=to_email,
    message= signup_message)
