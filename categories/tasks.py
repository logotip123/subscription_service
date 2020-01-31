from celery import shared_task
from django.core.mail import send_mass_mail

from django.conf import settings


@shared_task
def send_emails(subject: str, text: str, emails: list):
    messages = []
    for email in emails:
        message = (subject, text, settings.EMAIL_SENDER, [email])
        messages.append(message)
    send_mass_mail(messages, fail_silently=False)
    return None
