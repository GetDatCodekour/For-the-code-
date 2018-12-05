#!/usr/bin/env python

import sys
import sqlalchemy
from SQLiteConnection import engine, Session
from ModelClasses import *

from SQLite connection import engine,session









session = session(autoflush=False)

with open(args.input_file) as datafile:
  
  line=datafile.readlne()
  while line.syarwith('#'):
    line=datafile.readline()
    
   col_names=line.rstrip("\n").split('|')
  
  For line in datafile:
    values=line.rstrip().split('|')
    
  data=dict(zip(col_names,values))
  
  student=Student()
  student.first_name=data['first_name']
  student.last_name=data['last_name']
  session.add(student)
  
  try:
    status = session.query(Stauus).filter(statis.label==daa['status']).one()
  except sqlalchemy.orm.exc.NoResultFound:
    #status found, create a new one
    status=Status()
    status.label=data['status']
    session.add(status)
  except sqlalchemy.orm.exc.MultipleResultsFound:
    raise Exception("More than one result found in db - add a new status")
    
  student.status.append(status)
  
  #Same base code for city
  
  if len(data['club']) > 0:
    for club_name in data['club'].split(", "):
      try:
        club=session.quey(Club).filter(Club.name==club_label)
      except sqlalchemy.orm.exc.NoResultFound:
        club=Club()
        club.name=club_name
        clud.id=club_id
        session.add(club)
        
# filename = 'student_data.txt'
# or use argparse

# data = open(filename)

session = Session()


# your code here

session.commit()

engine.dispose() # cleanly disconnect from the database
sys.exit(0)


#Query this beyatch
print()
print("Attleboro students")
for studen in session.query(City).filter(City.label=="Attleboro").one().students:
  print(f"{student.first_name}{student.last_name}")

clubs=session.query(Club)
for club in clubs:
        
