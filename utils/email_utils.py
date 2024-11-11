import os
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def send_email_gmail_oauth(to_email, subject, content):
    """
    Send email using Gmail API with OAuth authentication.
    :param to_email: Recipient email address.
    :param subject: Email subject.
    :param content: Email body content.
    """
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            raise Exception("OAuth credentials missing or expired.")

    service = build('gmail', 'v1', credentials=creds)
    message = {
        'raw': base64.urlsafe_b64encode(
            f"Subject: {subject}\n\n{content}".encode("utf-8")
        ).decode("utf-8")
    }
    result = service.users().messages().send(userId="me", body=message).execute()
    print(f"Email sent to {to_email}: {result}")

