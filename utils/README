# CUSTOM EMAIL SENDER

## Project Overview
This project is designed to automate email scheduling and content generation. It integrates Gmail and SendGrid for sending emails and uses OpenAI's API for generating dynamic email content. The system allows users to schedule emails for later delivery and generates content based on user input or predefined templates.

## Features
Email Sending: Send emails via Gmail API or SendGrid, based on your configuration.
Email Scheduling: Schedule emails to be sent at a specific time.
Dynamic Content Generation: Automatically generate email content using OpenAI API.
Single-Database Configuration: Manage user data, email settings, and logs in one centralized database.
Flask Integration: Built with Flask for handling user authentication, web requests, and email scheduling.

## Prerequisites
Before setting up the project, make sure you have the following:
Python 3.7 or higher installed on your machine.
A Gmail API token.
A SendGrid API key.
An OpenAI API key for content generation.

## Project Setup

### 1. Folder Structure Explained:

main.py: Entry point for the Flask application.
config.py: Configuration for the app and database.
utils/: Helper functions for reading CSVs, Google Sheets, and email sending.
templates/: HTML templates for the frontend.
static/: Static files like CSS for styling.
models/: Database models for managing email scheduling data.
celery_tasks/: Celery tasks for handling email sending with rate limiting.
email_tracking/: Modules for integrating and tracking email delivery with SendGrid.
migrations/: Database migration files.

### 2. Install Dependencies
To set up the environment and install necessary dependencies, follow these steps:

1. Clone the repository:

git clone <your_repository_url>
cd <your_project_directory>



2. Create a virtual environment:
```python
python -m venv venv
```

3. Activate the virtual environment:

For Windows:
.\venv\Scripts\activate

For macOS/Linux:

source venv/bin/activate

4. Install the required packages:

````python
pip install -r requirements.txt
````
This will install all necessary dependencies such as Flask, SendGrid, Google OAuth, and OpenAI.

### 3. Environment Variables
To store sensitive data securely, create a .env file in your project directory and add the following variables:

SENDGRID_API_KEY=<Your_SendGrid_API_Key>
OPENAI_API_KEY=<Your_OpenAI_API_Key>
WEBHOOK_AUTH=<Basic Auth for Webhook>
GMAIL_CLIENT_SECRET=<Your_Gmail_Client_Secret>
Make sure to replace the placeholders (<Your_SendGrid_API_Key>, <Your_OpenAI_API_Key>, etc.) with your actual credentials.

### 4. Configuration
This project uses Flask for backend API handling and SQLite for managing user data and email logs. Ensure your database is set up and configured correctly. The following environment variables are required for the system:

SENDGRID_API_KEY: Your SendGrid API key for sending emails.
OPENAI_API_KEY: Your OpenAI API key for generating dynamic email content.
WEBHOOK_AUTH: A Basic Auth key for securing the webhook endpoint.
GMAIL_CLIENT_SECRET: The client secret from Google Developer Console for Gmail API access.

### 5. Running the Application
Once the dependencies are installed and the .env file is set up, you can run the Flask application.

1. Start the Flask development server:

```python
flask run
```

This will start the Flask server at http://127.0.0.1:5000/, where you can access the application in your browser.

2. View Scheduled Emails
To view the list of all scheduled emails with details like subject, prompt, and scheduled time:
Navigate to the following URL in your browser:

http://localhost:5000/view_emails

This will display a table of all scheduled emails with their subject, prompt content, and scheduled send time.

### 6. Authentication and Permissions
Gmail API: Follow the OAuth flow to obtain the necessary token.json for authentication.
SendGrid API: Create an API key in your SendGrid account and store it in the .env file.
OpenAI API: Ensure you have a valid OpenAI API key for content generation.

### 7. Using the Application
Once the application is running, here’s how to use it:
Email Scheduling: You can schedule emails to be sent later.
Content Generation: Use OpenAI's API to generate dynamic email content based on prompts.
Send Email: Emails can be sent using either Gmail or SendGrid, depending on your chosen configuration.

**Authors:**
TEJASWINI GUDIPATI

**License:**
MIT License
