#! /usr/bin/python3

import sqlite3
from datetime import date

# CREATE TABLE tasks (id, task, priority, severity, type, subtask, estimatedtime, creationdate, deadline, importance);


# determine id

conn = sqlite3.connect('todo.sqlite')
c = conn.cursor()

c.execute("select max(id) from tasks;")
maxid = c.fetchone()
print(maxid)

if maxid[0] == (None):
    id = 0;
else:
    id = int(maxid[0]) + 1;

task = input('Name of the task: ')
priority = input('Priority: ')
severity = input('Severity: ')
type = input('Type/Category: ')
subtask = input('Subtask: ')
estimatedtime = input('Estimated work time: ')
creationdate = date.isoformat(date.today())
deadline = input('Deadline: ')
importance = input('Importance: ')

print ("id, task, priority, severity, type, subtask, estimatedtime, creationdate, deadline, importance")
print (id, task, priority, severity, type, subtask, estimatedtime, creationdate, deadline, importance)

c = conn.cursor()
c.execute('INSERT INTO tasks VALUES (?,?,?,?,?,?,?,?,?,?)', [(id), (task), (priority), (severity), (type), (subtask), (estimatedtime), (creationdate), (deadline), (importance)])
conn.commit()

conn.close()
