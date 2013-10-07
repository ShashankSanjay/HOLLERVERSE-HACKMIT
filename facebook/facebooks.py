import config
from facepy import GraphAPI
import json
#import facebook

class facebooks:
	def __init__(self):
		c = config.config()
		self.access_token_Shashank = c.access_token_Shashank
		self.access_token_Moskie = c.access_token_Moskie
		self.access_token_Mike = c.access_token_Mike

		#self.graph = GraphAPI(self.access_token_Shashank)
		#self.graph.Moskie = GraphAPI(self.access_token_Moskie)
		#self.graph.Mike = GraphAPI(self.access_token_Mike)
		
	def getPostsShashank(self):
		self.graph = GraphAPI(self.access_token_Shashank)
		print(self.graph.get('me/posts'))

	def getPostsMoskie(self):
		self.graph = GraphAPI(self.access_token_Moskie)
		print(self.graph.get('me/posts'))

	def getPostsMike(self):
		self.graph = GraphAPI(self.access_token_Mike)
		print(self.graph.get('me/posts'))

	def findFriendShashank(self, theirname):
		graph = GraphAPI(self.access_token_Shashank)
		#graph.get('me/friends')
		json = graph.fql('SELECT uid, username, name, pic_square FROM user WHERE CONTAINS("Michael Moskie") and strpos(name, "Michael Moskie") >=0')
		for result in json['data']:
			if(theirname==result['name']):
				return(result['username'])
		return('whoops not found')

	def postFriendMoskie(self, uid):
		graph = GraphAPI(self.access_token_Shashank)
		graph.post("me/feed", retry=1, message=" @["+str(uid)+"]")
		#print(friends)
		#graph.post(path='https://graph.facebook.com/'+me+'/feed', retry=1, message="Hello")

