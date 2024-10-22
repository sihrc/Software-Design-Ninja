from git import Repo
import os, shutil
from models import *
from operator import itemgetter

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

def clone_repos(students, syspath=os.path.join("..","repos"), url="git@github.com:%s/SoftwareDesign.git"):
  """
  Recursively removes previous copies of the repo (requires user confirmation)
  Clones the repos from the urls to a folder called repos/<username>

    students : list of student objects
    syspath : system path to copy repos to
  """
  if (raw_input("Remove current repositories? (y/n) ")) != "y":
    raise Exception("Failed to confirm. Failed to clone repos")
  
  # if other repos exist, remove them
  if os.path.exists(syspath):
    shutil.rmtree(syspath) # remove existing repos
    print "Successfully removed repos from \"%s\"" % syspath

  for s in students:
    path = syspath + s.user
    
    print "Cloning Repo: %s to %s" % (s.name, path)

    if not os.path.exists(path):
      os.makedirs(path)
    
    Repo.clone_from(url % s.user, path)

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

def levenshtein(s1, s2):
  if len(s1) < len(s2):
    return levenshtein(s2, s1)
  if len(s2) == 0:
    return len(s1)
  if s1 in s2:
    return len(s2) - len(s1)
  previous_row = xrange(len(s2) + 1)
  for i, c1 in enumerate(s1):
    current_row = [i + 1]
    for j, c2 in enumerate(s2):
      insertions = previous_row[j + 1] + 1
      deletions = current_row[j] + 1      
      substitutions = previous_row[j] + (c1 != c2)
      current_row.append(min(insertions, deletions, substitutions))
    previous_row = current_row
 
  return previous_row[-1]

def crossReference(students,userse):
  match = dict()
  while len(students) > 0:
    full = students.pop()
    first = full[0]
    last = full[-1]
    for user in users:
      match[full] = match.get(full, []) + [(user, levenshtein(first,user))]
      match[full] = match.get(full, []) + [(user, levenshtein(last,user))]
    match[full].sort(key = itemgetter(1))
    match[full] = match[full][:2]
  return match

# aliases
test = test_urls
clone = clone_repos
pull = pull_repos