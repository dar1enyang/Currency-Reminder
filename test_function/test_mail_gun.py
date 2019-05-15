import requests

def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandboxcf0f0204481f4e5db32ca491987d150f.mailgun.org/messages",
		auth=("api", "b7288f39ae1c25d533325c5181e0eada-4a62b8e8-809b3b07"),
		data={"from": "Mailgun Sandbox <postmaster@sandboxcf0f0204481f4e5db32ca491987d150f.mailgun.org>",
			"to": "Po Yu Yang <stfu0520@gmail.com>",
			"subject": "Hello Po Yu Yang",
			"text": "Congratulations Po Yu Yang, you just sent an email with Mailgun!  You are truly awesome!"})


send_simple_message()