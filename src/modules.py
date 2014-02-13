import os

def createRefs(hw):
	for student in os.listdir("repos"):
		if "." in student:
			continue
		with open(os.path.join("repos", student, "__init__.py"), "wb") as f:
			for homework in os.listdir(os.path.join("repos", student)):
				if hw in homework:
					f.write("import " + homework + "\n")
					with open(os.path.join("repos", student, homework, "__init__.py"), 'wb') as g:
						for script in os.listdir(os.path.join("repos", student, homework)):
							if "." not in script:
								continue
							if ".py" == script[-3:]:
								g.write("import " + script[:-3] + "\n")		