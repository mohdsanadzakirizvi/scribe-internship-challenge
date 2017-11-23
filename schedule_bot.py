"""
file: schedule_bot.py
author: sanad(https://github.com/mohdsanadzakirizvi)
desc: scheduler bot code
license: MIT
"""
import slack_utility

def post_hi():
	"""
	Use slack_utility's send_message() function to post a hi message in general channel
	"""
	slack_utility.send_message(channel='#general', msg='hi')	

if __name__ == '__main__':
	post_hi()