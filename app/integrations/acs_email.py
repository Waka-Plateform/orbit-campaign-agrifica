from azure.communication.email import EmailClient
from app.config import Settings
class AcsEmailClient:
    def __init__(self, settings: Settings):
        self.client = EmailClient.from_connection_string(settings.acs_email_connection_string)
    def send(self, sender: str, to: str, subject: str, html: str):
        poller = self.client.begin_send({"senderAddress": sender, "recipients": {"to": [{"address": to}]}, "content": {"subject": subject, "html": html}})
        return poller.result()
