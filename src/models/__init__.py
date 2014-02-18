from students import * 
import os

def get_students_from_csv (path=os.path.join("..","data"), filename='students.csv'):
  '''
  import students from csv and create a list of Student objects
  '''
  students = []
  if not os.path.exists(path):
    os.makedirs(path)
  with open(os.path.join(path, filename), 'rb') as csvfile:
    reader = csv.reader(csvfile)

    header = reader.next()

    for row in reader:
      students.append(Student(**dict(zip(header, row))))

  return students, header

def get_students_from_json (path=os.path.join("..","data"), filename='students.json'):
  ''' get students from json
  hasn't been updated to use Students model
  '''
  students = {}
  if not os.path.exists(path):
    os.makedirs(path)
  with open(os.path.join(path, filename), 'rb') as jfile:
    students = json.load(jfile)

  return students

# aliases
gcsv = get_students_from_csv
gjson = get_students_from_json

students, header = gcsv()