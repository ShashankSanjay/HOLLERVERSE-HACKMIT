from twilio.rest import TwilioRestClient
import twilioconfig
import requests
import twiliohelp

class Twilio:
	
	def __init__(self):
		x = twilioconfig.config()
		self.twilionumber = x.twilionumber
		self.account_sid = x.account_sid
		self.auth_token = x.auth_token
		self.client = TwilioRestClient(x.account_sid, x.auth_token)

	def sms(self, messagetext, usernumber):
		message = self.client.messages.create(body=messagetext,
	    	to = usernumber,    # Replace with your phone number
	    	from_= self.twilionumber) # Replace with your Twilio number
		print message.sid

	def call(self, messagetext, tonumber):
		requests.post("https://api.twilio.com/2010-04-01/Accounts/" + self.account_sid + "/Calls.xml")
		t = twiliohelp.twiliohelp()
		self.voice = t.makeVoiceXML(messagetext, "robot")
		print(self.voice)
		call = self.client.calls.create(to=tonumber, from_=self.twilionumber, url=("http://shashanksanjay.com/hollerverse/"+str(self.voice)))
		print call.sid
