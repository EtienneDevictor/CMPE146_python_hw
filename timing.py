import time

def calculate_time(func):
	def wrapper():
		t = time.time()
		func()
		t = time.time() - t
		print(t)
	return wrapper


