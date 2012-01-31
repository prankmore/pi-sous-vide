import tornado.ioloop
import tornado.web
import threading

class MainHandler(tornado.web.RequestHandler):

	def get(self):
		self.render("template1.html", title="Sous Vide", temp=str(probe.readtemp()),target=str(control.gettarget()),power=str(control.Relay()))

	def post(self):
		control.settarget(int(self.get_argument("message")))
		control.UpdateControl()
		self.render("template1.html", title="Sous Vide", temp=str(probe.readtemp()),target=str(control.gettarget()),power=str(control.Relay()))

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
	def disable(self):
		self.controling=False
	def UpdateControl(self):
		print 'Timer update'
		temp=probe.readtemp()
		if(temp<self.targettemp):
			self.state=True
		else:
			self.state=False

	def Relay(self):
		return self.state



global t
probe=thermometer()
control=controller()

def hello():
	control.UpdateControl()
	t=threading.Timer(5.0,hello)
	t.start()




if __name__ == "__main__":
	application.listen(8888)
	t=threading.Timer(5.0,hello)
	t.start()
	tornado.ioloop.IOLoop.instance().start()


