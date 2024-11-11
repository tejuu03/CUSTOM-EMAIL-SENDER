from celery import Celery
from utils.email_utils import send_email_smtp
import time

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task
def send_email_task(data, rate_limit=10):
    """
    Send emails with rate limiting. Pauses after sending 'rate_limit' emails.
    :param data: List of email data containing recipient emails and other content.
    :param rate_limit: The number of emails to send before pausing (default is 10).
    """
    for i, entry in enumerate(data):
        # Send email with rate limiting by pausing between sends
        if i > 0 and i % rate_limit == 0:
            time.sleep(60)  # Sleep for 1 minute after sending 'rate_limit' emails
        send_email_smtp(entry['Email'], 'Subject', 'Message')

