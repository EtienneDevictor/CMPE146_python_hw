import time

def my_decorator(func):
	def wrapper():
		t = time.time()
		func()
		t = time.time() - t
		print(t)
	return wrapper


