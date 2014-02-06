import get_repos as git
import roster
import tests

class Tester:
	def __init__(self, cases = dict()):
		self.cases = cases

	def addArgs (self, result, **args):
		return **args


if __name__ == "__main__":
	students = roster.groupD
	#git.clone_repos(students.values()) # Initial Run Only
	git.pull_repos(students.values())

	for student in students:
		exec("import repos." + students.keys())