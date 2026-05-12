from app.integrations.acs_email import AcsEmailClient
def send_email(settings, sender, to, subject, html):
    return AcsEmailClient(settings).send(sender, to, subject, html)
