import sendgrid
from sendgrid.helpers.mail import Mail
from sendgrid.helpers.event import EventWebhook
import os

def send_with_sendgrid(to_email, subject, content):
    """
    Send an email using SendGrid's API.
    :param to_email: Recipient's email address.
    :param subject: Email subject.
    :param content: Email body content.
    :return: HTTP response code from SendGrid API.
    """
    try:
        sg = sendgrid.SendGridAPIClient(api_key=os.getenv('SENDGRID_API_KEY'))
        mail = Mail(from_email='your-email@example.com', to_emails=to_email, subject=subject, html_content=content)
        response = sg.send(mail)
        return response.status_code
    except Exception as e:
        print(f"Failed to send email: {e}")
        return None

def setup_webhook():
    """
    Set up SendGrid event webhook to track email delivery status.
    :return: EventWebhook object for configuration.
    """
    webhook = EventWebhook()
    webhook.set_event_urls(['your-webhook-url'])
    webhook.set_http_auth('basic', os.getenv('WEBHOOK_AUTH'))
    return webhook

