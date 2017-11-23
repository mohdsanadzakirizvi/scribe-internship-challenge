scribe-internship-challenge
===========================

The code contained in this repository is for Scribe's Internship Challenge. The task list can be found in 

## Project Structure
The following is the project structure:

 - .bash_profile : used to set environment variables
 - mainbot.py : main code of the slackbot
 - slack_utility.py : contains utility functions for the slackbot
 - schedule_bot.py : contains the schedule bot for Task #1
 
 ## Start Project
 
 1. Set the $SLACK_TOKEN environment variable 
 ```
 source .bash_profile
 ```
 2. Start the slackbot 
 ```python
 python mainbot.py
 ```
 3. Join the Slack Workplace
 ```
 https://sanadslacktest.slack.com/
 ```
 4. The botname is **@goldiloxbot**. Ask him to set a reminder for you
 ```
 @goldiloxbot set reminder please
 ```
 ![Alt text](/botimage.jpg?raw=true)
 
 ## Dependencies
 The project depends upon the following packages:
 
  - [slackclient](https://github.com/slackapi/python-slackclient)
  - [python-crontab](https://pypi.python.org/pypi/python-crontab)
  - [pytz](https://pypi.python.org/pypi/pytz)
  
 ## License
 
 MIT
