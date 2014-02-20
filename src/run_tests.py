import get_repos as git
import roster
import tests as Tester
import os

class Tester:
	def __init__(self, cases = dict()):
		self.cases = cases

	def addArgs (self, result, **args):
		return args

def test_func(func):
	def wrapper(*arg):
		t1 = time.time()
		res = func(*arg)
		t2 = time.time()
		print '%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.0)
		return res
	return wrapper
	
if __name__ == "__main__":
	students = roster.groupA
	git.get_repos(students.keys(), students)

	#for student, repo in students:
	#	exec("import repos." + repo)
	