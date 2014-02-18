import gitpy as git
import modules
import roster
import os

class Tester:
	def __init__(self, mod, functions = []):
		self.mod = mod
		self.functions = getFunctions(functions)
		self.tests = []

	def getFunctions(self, funcnames):
		funcs = dict()
		for name in funcnames:
			exec("funcs["+name+"] = self.mod." + name)
		return funcs

	def addTest(self, test):
		self.tests.append(self.functions[test.name], test)

	def runTests(self):
		results = []
		for func,test in self.tests:
				print "Testing", func.__name__, "..."
				success = func(test.arg) == test.results
				results.append(func.__name__, success)
				print "Success" if success else "Failed"
		return results

class Test:
	def __init__(self, name, args, results):
		self.name = name
		self.args = args
		self.results = results


if __name__ == "__main__":
	students = roster.groupD
	git.get_repos(students.keys(), students)
	#modules.createRefs("hw3")
	#import repos # this must be run after modules.createRefs
	#for student, repo in students.iteritems():
		#TO-DO RUN TESTS HERE - finish a better Tester Class
		# exec("import repos." + repo + ".hw3.gene_finder as source")
		# print "I'm doing something"
		# testManager = Tester(source, ["collapse", "coding_strand_to_AA", "coding_strand_to_AA_unit_tests", "get_reverse_complement", "get_reverse_completment", "rest_of_ORF", "rest_of_ORF_unit_tests", "find_all_ORFs_oneframe"])
		# Tester.addTest(Test("collapse", ["2","3","4"], "234"))
		# res = Tester.runTests()
		# print res


	