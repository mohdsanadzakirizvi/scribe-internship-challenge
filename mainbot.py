"""
file: mainbot.py
author: sanad(https://github.com/mohdsanadzakirizvi)
desc: contains primary code of the bot
license: MIT
"""
import slack_utility
import time

def parse_slack_response(rtm_output):
	"""
	Parse slack responses that are aimed at the bot else return None
	"""
	AT_BOT = '<@'+slack_utility.get_bot_id()+'>'
	if rtm_output and len(rtm_output):
		for output in rtm_output:
			if output and 'text' in output and AT_BOT in output['text']:
				return output['text'].split(AT_BOT)[1].strip(), output['channel']
	return None, None 

def handle_command(command, channel):
	"""
	Recieves commands directed for the bot, if they are valid perform action 
	else resends clarification
	"""
	EXAMPLE_COMMAND = 'do'
	if command.lower().startswith(EXAMPLE_COMMAND):
		slack_utility.send_message(msg='Yes, code me further to do that!')
	elif command.lower().startswith('set reminder'):
		slack_utility.send_message(msg='Hey, what\'s your timezone?')
	elif command.startswith('my timezone is'):
		tzone = command.split('my timezone is')[1].strip()
		slack_utility.create_cron(tzone)
	else:
		print 'Invalid Command: Not Understood'
		slack_utility.send_message(msg='Invalid Command: Not Understood')
	
def main():
	"""
	Initiate the bot and call appropriate handler functions
	"""
	READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
	slack_api = slack_utility.connect()
	if slack_api.rtm_connect():
		print 'SLACK_BOT connected and running'
		while True:
			command, channel = parse_slack_response(slack_api.rtm_read())
			if command and channel:
				handle_command(command, channel)
			time.sleep(READ_WEBSOCKET_DELAY)
	else:
		print('Connection failed. Invalid Slack token or bot ID?')

if __name__ == '__main__':
	main()