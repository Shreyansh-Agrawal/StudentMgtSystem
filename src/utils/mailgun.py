import os
from pathlib import Path

from dotenv import load_dotenv
import requests

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)
MAILGUN_DOMAIN = os.getenv('MAILGUN_DOMAIN')
MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY')


def send_simple_message(to, subject, body):
	return requests.post(
		f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
		auth=("api", MAILGUN_API_KEY),
		data={"from": f"Shreyansh Agrawal <mailgun@{MAILGUN_DOMAIN}>",
			"to": [to],
			"subject": subject,
			"text": body})
 