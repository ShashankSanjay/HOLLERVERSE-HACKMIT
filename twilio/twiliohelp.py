import uuid
import pysftp
import os
import sftpinfo
class twiliohelp:
	def __init__(self):
		print "twiliohelp"
		self.flin = sftpinfo.ftpinformation()
	def makevoiceXML(self,message,voice): #accepts voices man woman robot
		self.makeFile('<?xml version="1.0" encoding="UTF-8"?> <Response> <Say voice="'+str(voice).lower()+'">'+str(message)+ ' </Say> </Response>')

	def makeAudioFileXML(self,url,loop):
		self.makeFile('<?xml version="1.0" encoding="UTF-8"?> <Response> <Play loop="'+str(loop)+'">'+str(url)+ ' </play> </Response>')

	def makeRecordXML(self, timeout, transcribe):
		self.makeFile('<?xml version="1.0" encoding="UTF-8"?> <Response> <Record timeout="'+str(timeout)+' transcribe="'+str(transcribe)+' />')

	def makeFile(self,xml):
		unique_filename = uuid.uuid1()
		print unique_filename
		f = open(str(unique_filename),'w')
		f.write(xml)
		f.close();
		self.fileUpload(str(unique_filename))

	def fileUpload(self,fn):
		srv = pysftp.Connection('michaelmoskie.com',username=str(self.flin.user),password=str(self.flin.password))
		srv.put(fn)
		print "upload complete"
		srv.close()
		os.remove(fn)
