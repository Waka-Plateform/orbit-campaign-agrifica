from azure.communication.sms import SmsClient
from app.config import Settings
class AcsSmsClient:
    def __init__(self, settings: Settings):
        self.client = SmsClient.from_connection_string(settings.acs_sms_connection_string)
    def send(self, sender: str, to: str, message: str):
        return self.client.send(from_=sender, to=[to], message=message, enable_delivery_report=True)
