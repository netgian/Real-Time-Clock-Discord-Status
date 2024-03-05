from requests import Session
import time

TOKEN = "Account-Token"

def main(token):
    url = 'https://discord.com/api/users/@me/settings'
    headers = {'authorization': TOKEN, 'Content-Type': 'application/json'}
    emojis = '🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥🕚🕦'
    s = Session(headers=headers)
    
    while True:
    	hour = int(time.strftime('%H'))
    	mins = int(time.strftime('%M'))
    
    	emoji = emojis[((hour - 12)*2 if hour >= 12 else hour*2) + (1 if mins >= 30 else 0)]
    
    	payload = {
    		'custom_status': {
    			'text': time.strftime('%H:%M:%S'),
    			'emoji_name': emoji
    		}
    	}
    
    	s.patch(url, json=payload)
    	time.sleep(3)

if __name__ == "__main__":
    main(TOKEN)
