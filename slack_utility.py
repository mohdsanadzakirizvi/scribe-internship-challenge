"""
file: slack_utility.py
author: sanad(https://github.com/mohdsanadzakirizvi)
desc: contains utility functions for the project
license: MIT
"""
from slackclient import SlackClient
from datetime import datetime
from pytz import timezone
from crontab import CronTab
from os import environ

def connect():
	"""
	Initiate a connection to Slack API
	"""
	# API_KEY = get_slack_token()
	slack_api_client = SlackClient('xoxb-276075241505-r69fespKULLBFBDasQgrb24N')
	return slack_api_client

def get_users():
	"""
	Fetch a dictionary of username and their IDs from Slack
	"""
	slack_api_client = connect()
	api_call = slack_api_client.api_call('users.list')
	if api_call.get('ok'):
		user_list = dict([(x['name'], x['id']) for x in api_call['members']])
		return user_list
	else:
		print 'Error Fetching Users'
		return None

def get_bot_id(botname='goldiloxbot'):
	"""
	Get BOT_ID using botname and set in the env variable BOT_ID
	"""
	if environ.get('SLACK_BOT_ID'):
		return environ.get('SLACK_BOT_ID')
	else:
		user_list = get_users()
		if user_list:
			BOT_ID = user_list[botname]
			environ.update({'SLACK_BOT_ID': BOT_ID})
			return BOT_ID
		else:
			print 'BOTNAME not present in user list'
			return None

def get_slack_token():
	"""
	Get SLACK_TOKEN from environment variable
	"""
	if environ.get('SLACK_TOKEN'):
		return environ.get('SLACK_TOKEN')
	else:
		print 'SLACK_TOKEN not set in the environment'
		return None
	
def send_message(channel='#general', msg='Bot Testing'):
	"""
	Send given text message to the slack #general channel
	"""
	slack_api_client = connect()
	if slack_api_client.rtm_connect():
		slack_api_client.rtm_send_message(channel, msg)

def convert_by_timezone(tzone):
	"""
	Convert 12PM in their timezone to IST
	"""
	date_timezone = datetime.strptime('12:00:00','%H:%M:%S')
	date_timezone = timezone(tzone).localize(date_timezone)
	date_ist = date_timezone.astimezone(timezone('Asia/Kolkata'))
	return date_ist.hour

def create_cron(tzone):
	"""
	Create or update cron job to schedule the bot
	"""
	hour_in_ist = convert_by_timezone(tzone)
	job_comment = 'slack_schedule_bot'
	cron_tab = CronTab(user='sanad')
	for job in cron_tab:
		if job.comment == job_comment:
			break
	else:
		cron_job = cron_tab.new(command='/usr/local/bin/python /Users/sanad/development/scribe-internship-challenge/schedule_bot.py', comment=job_comment)
		cron_job.minute.on(0)
		cron_job.hour.on(hour_in_ist)
		cron_tab.write()
		print 'Cron sucessfully created'
	print 'Cron already exists'
	send_message(msg='Reminder Set for Everyday at '+str(hour_in_ist)+':00PM IST')
	



