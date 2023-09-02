from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'AC6c67a00edff430a271167dec35efd123'
auth_token = 'b39a8560af5c76f176b66d9e6f52f300'

# Your Twilio Phone Number
twilio_phone_number = '+13186180445'

# Recipient's Phone Number
recipient_phone_number = '+918248537952'  # Replace with the recipient's actual phone number

# Create a Twilio client
client = Client(account_sid, auth_token)

# Define the custom message with a clickable link
custom_message = 'Hey, check out this link: http://example.com/download.png'

# Send the SMS message with the custom message
message = client.messages.create(
    body=custom_message,
    from_=twilio_phone_number,
    to=recipient_phone_number
)

print(f'Message sent to {recipient_phone_number}: {custom_message}')
