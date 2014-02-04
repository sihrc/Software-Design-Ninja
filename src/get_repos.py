from git import Repo
import os, shutil

def test_urls (users, url="https://github.com/%s/SoftwareDesign"):
	"""
	Test whether or not the urls are valid
	"""
	import urllib2

	failed = [] # keep track of failed user ids
	
	for uid in users:
		try:
			urllib2.urlopen(url % uid)
		except:
			failed.append(uid)
			print uid + " has failed to load"
	
	print "Loaded %i of %i successfully" % (len(users) - len(failed), len(users))
	print "Failed user ids: %s" % failed

def clone_repos(users, syspath="../repos/", url="https://github.com/%s/SoftwareDesign"):
	"""
	Recursively removes previous copies of the repo (requires user confirmation)
	Clones the repos from the urls to a folder called repos/<username>

		users : list of github ids
		syspath : system path to copy repos to
	"""
	if (raw_input("Remove current repositories? (y/n) ")) != "y":
		raise Exception("Failed to confirm. Failed to clone repos")
	
	# if other repos exist, remove them
	if os.path.exists(syspath):
		shutil.rmtree(syspath) # remove existing repos
		print "Successfully removed repos from \"%s\"" % syspath

	for uid in users:
		path = syspath + uid
		repo_url = url + ".git"
		
		print "Cloning Repo: %s to %s" % (uid, path)

		if not os.path.exists(path):
			os.makedirs(path)
		
		Repo.clone_from(url % uid, path)

	print "Successfully cloned repos"

def pull_repos(syspath="../repos/"):
	"""
	Pulls from remote for all directories under syspath
	"""
	for fold in os.listdir(syspath):
		print "Pulling Repo for ", fold
		repo = Repo(os.path.join(syspath,fold))

		o = repo.remotes.origin
		o.pull()

if __name__ == "__main__":
	# all users
	users =["acejang1994", "aloverso", "AmandaSutherland", "atproofer", "bishiguro", "cbauerswald", "cebeery", "cwallac", "daouani", "dcelik", "ddiggins", "dennis-chen", "dimitdim", "dinopants174", "doyunglee", "eengel", "emocallaghan", "flymperopoulos", "gabriellee", "gregcole", "griffint", "gubbatuba", "hpelletier", "HWilk", "hzhugit", "iangmhill", "InseongJoe", "jabb1123", "jagreene", "JenniferLVaccaro", "jenwei", "jmorris1993", "jsapers", "jwoo1123", "ksuzy31", "kyflores", "logandavis", "lvanderlyn", "mafaldaborges", "maorbernstein", "MJAFort", "mortier", "ndhanushkodi", "pencilEraser", "PMKeene", "Pratool", "ptitchener", "RRameshwar", "runnersaw", "rvanderheyde", "segerphilip", "SeongHyeok", "sgrim3", "shrinidhit", "srli", "ssingal05", "swalters4925", "themythicaldrago", "yunhsincynthiachen"]
	print "Current Number of repos: ", len(users)

	# test_urls(users)
	# clone_repos(users) # currently having issues with creating repos directory
