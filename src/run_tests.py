import get_repos as git
import roster
import tests

import os

class Tester:
	def __init__(self, cases = dict()):
		self.cases = cases

	def addArgs (self, result, **args):
		return args


if __name__ == "__main__":
	students = roster.groupD
	
	if not os.path.exists("../repos"):
		git.clone_repos(students.values()) # Initial Run Only
	else:
		print students.values()
		git.pull_repos()

	for student in students:
		exec("import repos." + students.keys())