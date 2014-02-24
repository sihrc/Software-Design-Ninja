import time
"""
* Debug/Timer Wrapper
	prints debug statements
	prints the timing of a function

author: chris
"""
def debug(func):
	def wrapper(*arg, **kwargs):
		print "======================================="
		print "Currently Running:",func.func_name
		t1 = time.time()
		res = func(*arg,**kwargs)
		t2 = time.time()
		print '%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.0)
		print "=======================================\n"
		return res
	return wrapper
