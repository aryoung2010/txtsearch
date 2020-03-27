# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC5a983eae4cfd86f5b3b47b8ab4294da8'
auth_token = '17ac87e6fecd0a9cca5f8cfb359082f6'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body="What can I help you find?",
         messaging_service_sid='MGcfe1deca92a725eba0cd276f9527cc43',
         to='+17045647984'
     )

print(message.sid)
