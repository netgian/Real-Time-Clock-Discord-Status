import requests
import time



TOKEN = 'Put your token here'
url = 'https://discord.com/api/users/@me/settings'
headers = {'authorization': TOKEN, 'Content-Type': 'application/json'}
clocks = '🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥🕚🕦'


while True:
	hour = int(time.strftime('%H'))
	mins = int(time.strftime('%M'))

	index = ((hour - 12)*2 if hour >= 12 else hour*2) + (1 if mins >= 30 else 0)
	clock = clocks[index]

	payload = {
		'custom_status': {
			'text': time.strftime('%H:%M:%S'),
			'emoji_name': clock
		}
	}

	requests.patch(url, headers=headers, json=payload)
	time.sleep(3)
