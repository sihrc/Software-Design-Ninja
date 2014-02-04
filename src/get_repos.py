from git import Repo
import os, shutil

urls =["https://github.com/acejang1994/SoftwareDesign", "https://github.com/aloverso/SoftwareDesign", "https://github.com/AmandaSutherland/SoftwareDesign", "https://github.com/atproofer/SoftwareDesign", "https://github.com/bishiguro/SoftwareDesign", "https://github.com/cbauerswald/SoftwareDesign", "https://github.com/cebeery/SoftwareDesign", "https://github.com/cwallac/SoftwareDesign", "https://github.com/daouani/SoftwareDesign", "https://github.com/dcelik/SoftwareDesign", "https://github.com/ddiggins/SoftwareDesign", "https://github.com/dennis-chen/SoftwareDesign", "https://github.com/dimitdim/SoftwareDesign", "https://github.com/dinopants174/SoftwareDesign", "https://github.com/doyunglee/SoftwareDesign", "https://github.com/eengel/SoftwareDesign", "https://github.com/emocallaghan/SoftwareDesign", "https://github.com/flymperopoulos/SoftwareDesign", "https://github.com/gabriellee/SoftwareDesign", "https://github.com/gregcole/SoftwareDesign", "https://github.com/griffint/SoftwareDesign", "https://github.com/gubbatuba/SoftwareDesign", "https://github.com/hpelletier/SoftwareDesign", "https://github.com/HWilk/SoftwareDesign", "https://github.com/hzhugit/SoftwareDesign", "https://github.com/iangmhill/SoftwareDesign", "https://github.com/InseongJoe/SoftwareDesign", "https://github.com/jabb1123/SoftwareDesign", "https://github.com/jagreene/SoftwareDesign", "https://github.com/JenniferLVaccaro/SoftwareDesign", "https://github.com/jenwei/SoftwareDesign", "https://github.com/jmorris1993/SoftwareDesign", "https://github.com/jsapers/SoftwareDesign", "https://github.com/jwoo1123/SoftwareDesign", "https://github.com/ksuzy31/SoftwareDesign", "https://github.com/kyflores/SoftwareDesign", "https://github.com/logandavis/SoftwareDesign", "https://github.com/lvanderlyn/SoftwareDesign", "https://github.com/mafaldaborges/SoftwareDesign", "https://github.com/maorbernstein/SoftwareDesign", "https://github.com/MJAFort/SoftwareDesign", "https://github.com/mortier/SoftwareDesign", "https://github.com/ndhanushkodi/SoftwareDesign", "https://github.com/pencilEraser/SoftwareDesign", "https://github.com/PMKeene/SoftwareDesign", "https://github.com/Pratool/SoftwareDesign", "https://github.com/ptitchener/SoftwareDesign", "https://github.com/RRameshwar/SoftwareDesign", "https://github.com/runnersaw/SoftwareDesign", "https://github.com/rvanderheyde/SoftwareDesign", "https://github.com/segerphilip/SoftwareDesign", "https://github.com/SeongHyeok/SoftwareDesign", "https://github.com/sgrim3/SoftwareDesign", "https://github.com/shrinidhit/SoftwareDesign", "https://github.com/srli/SoftwareDesign", "https://github.com/ssingal05/SoftwareDesign", "https://github.com/swalters4925/SoftwareDesign", "https://github.com/themythicaldrago/SoftwareDesign", "https://github.com/yunhsincynthiachen/SoftwareDesign"]

def test_urls (urls):
	"""
	Test whether or not the urls are valid
	"""
	import urllib2

	failed = []
	for each in urls:
		try:
			urllib2.urlopen(each)
		except:
			failed.append(each)
			print each + " has failed to load"
	print "loaded " + str(len(urls) - len(failed)) + " of " + str(len(urls)) + " successfully"
	print failed

def get_username(url):
	"""
	Extracts the username of the student from the github url
	"""
	return url[url.find("com/") + 4:url.find("/SoftwareDesign")]

def clone_repos(urls):
	"""
	Recursively removes previous copies of the repo (requires user confirmation)
	Clones the repos from the urls to a folder called repos/<username>
	"""
	if (raw_input("Remove current repositories?")) != "y":
		return "Failed"
	shutil.rmtree("../repos/")
	for url in urls:
		name = get_username(url)
		path = "../repos/" + name
		print "Cloning Repo: ", url, "\n to ", path
		if not os.path.exists(path):
			os.makedirs(path)
		Repo.clone_from(url + ".git", "../repos/" + name)
	return "Successful"

def pull_repos():
	"""
	Pulls from remote for all directories under "../repos/"
	"""
	home = "../repos/"
	for fold in os.listdir(home):
		print "Pulling Repo for ", fold
		repo = Repo(os.path.join(home,fold))
		o = repo.remotes.origin
		o.pull()


if __name__ == "__main__":
	#print clone_repos(urls)
	pull_repos()
