import tornado.ioloop
import tornado.web
from threading import Timer



class MainHandler(tornado.web.RequestHandler):

	def get(self):
		self.render("template1.html", title="My title", temp=str(probe.readtemp()),target=str(control.gettarget()),power=str(control.Relay()))

	def post(self):
		control.settarget(int(self.get_argument("message")))
#		control.UpdateControl()
		self.render("template1.html", title="My title", temp=str(probe.readtemp()),target=str(control.gettarget()),power=str(control.Relay()))

application = tornado.web.Application([
    (r"/", MainHandler),
	
])



class thermometer():
    currenttemp=30
    def readtemp(self):
	self.currenttemp=self.currenttemp+1
	return self.currenttemp



class controller():
	targettemp=5
	controling=True
	state=False
	def gettarget(self):
		return self.targettemp
	def settarget(self,newtarget):
		if(newtarget!=self.targettemp):
			self.targettemp=newtarget
	def enable(self):
		self.controling=True
		self.t=Timer(20,self.UpdateControl)
		self.t.start()
	def disable(self):
		self.controling=False
	def UpdateControl(self):
		print 'Timer update'
		temp=probe.readtemp()
		if(temp>self.targettemp):
			self.state=True
		else:
			self.state=False
		if(self.controling):
			self.t.start()
	def Relay(self):
		return self.state

probe=thermometer()
control=controller()



if __name__ == "__main__":
	application.listen(8888)
	control.enable()
	tornado.ioloop.IOLoop.instance().start()


