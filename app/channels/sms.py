from app.integrations.acs_sms import AcsSmsClient
def send_sms(settings, sender, to, body):
    return AcsSmsClient(settings).send(sender, to, body)
