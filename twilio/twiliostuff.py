from twilio.rest import TwilioRestClient
import config
import requests

class Twilio:
	
	def __init__(self):
		x = config.Twilioconfig()
		self.twilionumber = x.twilionumber
		self.account_sid = x.account_sid
		self.auth_token = x.auth_token
		self.client = TwilioRestClient(x.account_sid, x.auth_token)
		self.url = "http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient"

	def sms(self, messagetext, usernumber):
		message = self.client.messages.create(body=messagetext,
	    	to = usernumber,    # Replace with your phone number
	    	from_= self.twilionumber) # Replace with your Twilio number
		print message.sid

	def call(self, tonumber):
		requests.post("https://api.twilio.com/2010-04-01/Accounts/" + self.account_sid + "/Calls.xml")
		call = self.client.calls.create(to=tonumber, from_=self.twilionumber, url=self.url)
		print call.sid
