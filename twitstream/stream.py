import tweepy
import time
import twitterinfo
class tweeter:
	def __init__(self):
		x = twitterinfo.twitterinfo()
		self.consumer_key = x.consumerkey
		self.consumer_secret = x.consumersec
		self.access_token_key = x.accesstoken
		self.access_token_secret = x.accesssecret
		self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		self.auth.set_access_token(self.access_token_key, self.access_token_secret)
		self.api = tweepy.API(self.auth)
	
	def sendTweet(self,user,message):
		msg = str(user)+" "+message
		self.api.update_status(msg)

	def blastTweet(self,me,message):
		for user in tweepy.Cursor(self.api.followers,screen_name=me).items():
			print user.screen_name
			self.api.update_status(message+"@"+str(user.screen_name))




