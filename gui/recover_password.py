import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

API_KEY = os.getenv('SENDGRID_API_KEY')

def send_email(to_email, code):
    message = Mail(
        from_email='your_verified_email@example.com',
        to_emails=to_email,
        subject='Your Password Reset Code',
        plain_text_content=f'Your reset code is: {code}'
    )

    try:
        sg = SendGridAPIClient(API_KEY)
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        print(f"Error: {e}")