import threading,time
def function(t,d):
	while True:
		time.sleep(d)
		print("current thread name is %s" %t)
class Dummy(threading.Thread):
	def __init__(self,threadname,delaytime):
		threading.Thread.__init__(self)
		self.threadname=threadname
		self.l=[1,2,3]
		self.delaytime=delaytime
		self.start()
	def run(self):
		function(self.threadname,self.delaytime)

obj1=Dummy("Thread-1",2)
obj2=Dummy("Thread-2",5)


#steps: obj.start(args)-->run--->target=function