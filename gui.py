import wxversion
import sys
wxversion.select("2.8")
import wx
sys.path.insert(0,'twitstream')
sys.path.insert(0,'sendgrid')
sys.path.insert(0,'facebook')
sys.path.insert(0,'twilio')
import twiliohelp
import twiliostuff
import stream
import sendgridstuff

class main(wx.Frame): #Main Frame
	def __init__(self,parent,id):
		x = wx.GetDisplaySize()
		winsizex = x[0]/4+200
		winsizey = x[1]/4
		styler = wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER
		wx.Frame.__init__(self,parent,id,'HollerVerse',size=(winsizex,winsizey),pos=(0,20), style=styler)
		panel = wx.Panel(self)
		print winsizex
		print winsizey
		self.posCtrlholler = wx.TextCtrl(panel, -1, "", pos=(winsizex/2/2.436464088, winsizey/2/2.214285714), size=(winsizex/1.293255132,-1))
		self.posCtrlsubj = wx.TextCtrl(panel, -1, "", pos=(winsizex/2/2.436464088, winsizey/2/7.982621083), size=(winsizex/1.293255132,-1))
		self.posCtrlphone = wx.TextCtrl(panel, -1, "", pos=(winsizex/2/2.436464088, winsizey/2/1.28), size=(winsizex/1.293255132,-1))
		self.posCtrlem = wx.TextCtrl(panel, -1, "", pos=(winsizex/2/2.436464088, winsizey/2*1.1), size=(winsizex/1.293255132, -1))
		self.posCtrltw = wx.TextCtrl(panel, -1, "", pos=(winsizex/2/2.436464088, winsizey/2*1.4), size=(winsizex/1.293255132, -1))
		#self.btnfb = wx.BitmapButton(panel, -1, wx.Bitmap('facebook_icon.png'), pos=(winsizex/4/3.127659574,winsizey/4*2.041666667), size=(38,38))
		#self.btntw = wx.BitmapButton(panel, -1, wx.Bitmap('twitter_icon.png'), pos=(winsizex/4,winsizey/4*2.041666667), size=(38,38))
		#self.btnsms = wx.BitmapButton(panel, -1, wx.Bitmap('sms_icon.png'), pos=(winsizex/4*1.907029478,winsizey/4*2.041666667), size=(38,38))
		#self.btncall = wx.BitmapButton(panel, -1, wx.Bitmap('call_icon.png'), pos=(winsizex/4*2.678004535,winsizey/4*2.041666667), size=(38,38))
		#self.btnemail = wx.BitmapButton(panel, -1, wx.Bitmap('gmail_icon.png'), pos=(winsizex/4*3.448979592,winsizey/4*2.041666667), size=(38,38))
		self.btnholler = wx.Button(panel, -1, "HOLLER", (winsizex/4*1.589569161, winsizey/4*3.38333333))
		self.subjectlbl = wx.StaticText(panel, -1, "subject: ", pos=(winsizex/4/14, winsizey/4/3.5))
		self.hollerlbl = wx.StaticText(panel, -1, "HOLLER: ", pos=(winsizex/4/14, winsizey/4*1.00833333))
		self.phonelbl = wx.StaticText(panel, -1, "phone: ", pos=(winsizex/4/14, winsizey/4*1.60))
		self.emailbl = wx.StaticText(panel, -1, "email: ", pos=(winsizex/4/14, winsizey/4*2.20))
		self.twitterlbl = wx.StaticText(panel, -1, "twitter handle: ", pos=(winsizex/4/14, winsizey/4*2.8))
		#self.btnfb.Bind(wx.EVT_BUTTON,self.facebook)
		#self.btntw.Bind(wx.EVT_BUTTON,self.twitter)
		#self.btnsms.Bind(wx.EVT_BUTTON,self.sms)
		#self.btncall.Bind(wx.EVT_BUTTON,self.call)
		#self.btnemail.Bind(wx.EVT_BUTTON,self.email)
		self.btnholler.Bind(wx.EVT_BUTTON,self.holla)
		self.thetwitter = stream.tweeter()
		self.twilio = twiliostuff.Twilio()
		self.sendgrid = sendgridstuff.sendgridstuff()
		self.Show()

	def facebook(self,event):
		print event

	def twitter(self,event):
		print event
		if(str(self.posCtrlat.GetValue())=="EVERYONE"):
			self.thetwitter.blastTweet("@HollerVerse",str(self.posCtrlmsg.GetValue()))
		else:
			self.thetwitter.sendTweet(str(self.posCtrlmsg.GetValue()),str(self.posCtrlat.GetValue()))

	def sms(self,event):
		print event
		self.twilio.sms(str(self.posCtrlmsg.GetValue()),str(self.posCtrlat.GetValue()))

	def call(self,event):
		self.twilio.makeCall('+1'+str(self.posCtrlat.GetValue()),str(self.posCtrlmsg.GetValue()))
	
	def email(self,event):
		self.sendgrid.mail("hollerverse@gmail.com", str(self.posCtrlat.GetValue()),"Balls", "SUBJECTIFY", str(self.posCtrlmsg.GetValue()))
		
		

	def holla(self,event):
		print "holler holler, it's murdaaa"
		if(str(self.posCtrlphone.GetValue())):
			self.twilio.sms(str(self.posCtrlholler.GetValue()),str(self.posCtrlphone.GetValue()))
		if(str(self.posCtrlem.GetValue())):
			self.sendgrid.mail("hollerverse@gmail.com", str(self.posCtrlem.GetValue()),str(self.posCtrlem.GetValue()), str(self.posCtrlsubj.GetValue()), str(self.posCtrlholler.GetValue()))
		if(str(self.posCtrltw.GetValue())):
			if(str(self.posCtrltw.GetValue())=="EVERYONE"):
				self.thetwitter.blastTweet("@HollerVerse",str(self.posCtrlholler.GetValue()))
			else:
				self.thetwitter.sendTweet(str(self.posCtrlholler.GetValue()),str(self.posCtrltw.GetValue()))


if __name__=='__main__':
	app=wx.PySimpleApp()
	frame = main(parent=None,id = -1)
	frame.Show()
	app.MainLoop()


