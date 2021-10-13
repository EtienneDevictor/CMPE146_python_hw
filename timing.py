import time

def calculate_time(func):
	def wrapper():
		t = time.time()
		func()
		t = time.time() - t
		print(f'Total time {t}')
	return wrapper


