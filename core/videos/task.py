from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from videos import views
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task(bind=True)
def send_mail_func(self, top3):
    
    for user in top3:
        mail_subject = "Hi! Celery Testing about videos views rank."
        message = "Your video - "+ user["title"] +" is in top 3, and got "+ str(user["numViews"]) +"views.!"
        to_email = user["email"]
        #print (to_email)
        send_mail(
            subject = mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    
    
    return "Done"