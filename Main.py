from twilio.rest import Client
import random

# Your Twilio Account SID and Auth Token
account_sid = 'AC6c67a00edff430a271167dec35efd123'
auth_token = 'b39a8560af5c76f176b66d9e6f52f300'

# Your Twilio Phone Number
twilio_phone_number = '+13186180445'

# Recipient's Phone Number
recipient_phone_number = '+919344166795'  # Replace with the recipient's actual phone number

# Number of times to send the message
num_messages = 5

# Create a Twilio client
client = Client(account_sid, auth_token)

# Define Custom Message
custom_message = f'Hey Your Mobile is Hacked Shahina!!! To Unblock give a kiss to Karthick'

# Link to include in the message
link = 'C:\My_Projects\Otp_Sender\download.png'  # Replace with your actual link


# Compose and send the SMS message multiple times
for _ in range(num_messages):
    # Generate a random OTP (6-digit number)
    otp = str(random.randint(100000, 999999))
    
    # Include the OTP in the custom message
    message_content = f'{custom_message} Your OTP is: {otp}. Click here to unblock:'
    
    # Send the SMS message
    message = client.messages.create(
        body=message_content,
        from_=twilio_phone_number,
        to=recipient_phone_number
    )
    
    print(f'SMS sent to {recipient_phone_number}: {message_content}')
