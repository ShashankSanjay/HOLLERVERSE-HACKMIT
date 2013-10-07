import config
import sendgrid

class sendgridstuff:
	def __init__(self):
		c = config.config()
		self.username = c.username
		self.password = c.password

	def mail(self, myemail, email, name, messagesubject, messagebody):
		s = sendgrid.Sendgrid(self.username, self.password, secure=True)
		message = sendgrid.Message(myemail, messagesubject, messagebody,
		    '<p>'+messagebody+'</p>')
		# add a recipient
		
		message.add_to(email, name)

		# use the Web API to send your message
		s.web.send(message)
