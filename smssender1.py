from twilio.rest import Client
import time

# Your Twilio Account SID and Auth Token
ACCOUNT_SID = 'Your_Account_SID'
AUTH_TOKEN = 'Your_Auth_Token'

# Initialize the Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Function to send SMS
def send_sms(to, message):
    try:
        message = client.messages.create(
            body=message,
            from_='Your_Twilio_Phone_Number',
            to=to
        )
        print(f'SMS sent to {to} with SID: {message.sid}')
        return True
    except Exception as e:
        print(f'Error sending SMS to {to}: {str(e)}')
        return False

# Main function
def main():
    recipient_phone = '+1234567890'  # Replace with the recipient's phone number
    message_text = 'Hello, this is a test message from SMSApp.'
    
    if send_sms(recipient_phone, message_text):
        # Add code to update the progress bar
        print('SMS sent successfully.')
    else:
        # Add code to display an error notification
        print('Failed to send SMS.')

if __name__ == "__main__":
    main()
