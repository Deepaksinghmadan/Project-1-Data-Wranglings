class A:
	def __init__(self):
		print("Parent initiation")

class B(A):
	def fun(self):
		super().__init__()
		print("child initiation")

objB= B()
