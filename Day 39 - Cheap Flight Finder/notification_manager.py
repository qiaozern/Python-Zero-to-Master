from twilio.rest import Client

TWILIO_SID = "AC10c0f590d3118a16821715aae2c053a5"
TWILIO_AUTH = "6662995a3b6f0d0d3e61856b863516fb"
TWILIO_VISUAL_NUMBER = "+18059181349"
TWILIO_VERIFY_NUMBER = "+66955429616"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH)
    
    def send_sms(self, message):
        message = self.client.messages.create(
                     body=message,
                     from_=TWILIO_VISUAL_NUMBER,
                     to=TWILIO_VERIFY_NUMBER
                 )
        print(message.sid)