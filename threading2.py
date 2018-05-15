import threading,time
def function(t,d,number):
	while True:
		time.sleep(d)
		lock.acquire()
		print("current thread name is %s" %t)
		lock.release()

class Dummy(threading.Thread):
	def __init__(self,threadname,delaytime):
		threading.Thread.__init__(self)
		self.threadname=threadname
		self.n=n
		self.delaytime=delaytime
		self.start()
	def run(self): #its mandaory function in threading
		print("\n Thread %s is created.\n" %self.threading)
		function(self.threadname,self.delaytime,self)

obj1=Dummy("Thread-1",2)
obj2=Dummy("Thread-2",5)
lock=threading.lock() #very important in fraud prevention


#steps: obj.start(args)-->run--->target=function
#locking function use to protect simultaneus booking in threading
#Eg l=obj1.Lock()
#l.acquire()

#--------
#l.release()
#threading has shared memory whereas multiprocessing has multiple dedicated memory spaces simultaneously