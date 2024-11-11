import openai
from celery import Celery
from utils.email_utils import send_email_smtp

# Initialize the OpenAI API
openai.api_key = os.getenv('OPENAI_API_KEY')

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task
def send_email_task(headers, email_data, subject, prompt):
    """
    Generate email content dynamically using LLM (OpenAI API) and send emails.
    :param headers: List of column headers from the CSV data.
    :param email_data: List of rows from the CSV data.
    :param subject: Email subject.
    :param prompt: Customizable prompt for content generation.
    """
    for row in email_data:
        # Replace placeholders with actual data
        content = prompt
        for index, header in enumerate(headers):
            content = content.replace(f"{{{header}}}", row[index])

        # Use OpenAI to enhance the email content
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=content,
            max_tokens=100
        )
        custom_content = response['choices'][0]['text']
        
        send_email_smtp(row['Email'], subject, custom_content.strip())
        print(f"Email sent to {row['Email']}")


