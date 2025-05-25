from twilio.rest import Client
import os

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_PHONE_NUMBER')

client = Client(account_sid, auth_token)

def send_whatsapp_message(to, message):
    client.messages.create(
        body=message,
        from_='whatsapp:' + twilio_number,
        to='whatsapp:' + to
    )
