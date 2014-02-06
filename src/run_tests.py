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
	git.get_repos(students.keys(), students)

	# for student, repo in students:
	# 	exec("import repos." + repo)