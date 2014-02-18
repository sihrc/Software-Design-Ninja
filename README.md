Software-Design-Ninja
=====================

Repository for Software Design Ninjas


Requires GitPython

``` 
[sudo] pip install gitpython
```

## Usage

`main.py` is the new main module to use when cloning/pulling from students' repos. 

Save students manually to students.csv with a header row that follows the following scheme:
```
github,id,last,first,middle,regStatus,regDate,email,major,year
```
The major ones you should really care about are these attributes:
```
github
last
first
email
```

All `gitpython` functions have been aliased to follow your regular Git commands:
```
test = test_urls
clone = clone_repos
pull = pull_repos
```