import sendgridconfig
import sendgrid

class sendgridstuff:
	def __init__(self):
		c = sendgridconfig.config()
		self.username = c.username
		self.password = c.password
		self.sendgrid = sendgrid.Sendgrid(self.username, self.password, secure=True)

	def mail(self, myemail, email, name, messagesubject, messagebody):
		print("ayo mail!")
		message = sendgrid.Message(myemail, messagesubject, messagebody,
		    '<p>'+messagebody+'</p>')
		# add a recipient
		
		message.add_to(email, name)

		# use the Web API to send your message
		self.sendgrid.web.send(message)
