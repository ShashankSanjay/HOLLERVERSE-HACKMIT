import uuid
import os
import sftpinfo
import ftplib
from twilio import twiml

class twiliohelp:
	def __init__(self):
		print "twiliohelp"
		self.flin = sftpinfo.ftpinformation()

	def makeVoiceXML(self,message,voice): #accepts voices man woman robot
		r = twiml.Response()
		r.say(str(message))
		return (self.makeFile(str(r)))

	def makeAudioFileXML(self,url,loop):
		r = twiml.Response()
		r.play(str(url), str(loop))

		self.makeFile(str(r))

	def makeRecordXML(self, timeout, transcribe):
		self.makeFile('<?xml version="1.0" encoding="UTF-8"?> <Response> <Record timeout="'+str(timeout)+' transcribe="'+str(transcribe)+' />')

	def makeFile(self,xml):
		unique_filename = str(uuid.uuid1())+".xml"
		print unique_filename
		f = open(str(unique_filename),'w')
		f.write(xml)
		f.close();
		return (self.fileUpload(str(unique_filename)))

	def fileUpload(self,fn):
		print(self.flin.url, self.flin.user, self.flin.password)

		srv = ftplib.FTP(self.flin.url, self.flin.user, self.flin.password)
		srv.cwd("public_html/hollerverse")
		files = open(fn, 'r')
		srv.storbinary("STOR "+fn, files)
		srv.close()
		os.remove(fn)
		return (fn)
