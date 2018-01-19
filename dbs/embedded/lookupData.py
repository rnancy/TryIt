import sqlite3
from prettytable import *
from database import Database



#db = Database('todo.db')

#db_filename = 'todo.db'

#with sqlite3.connect(db_filename) as conn:
with Database('todo.db') as db:
       # cursor = conn.cursor()

        #cursor.execute("""
        #select id, priority, details, status, deadline from task where project = 'pymotw'
        #""")
        db.query("select details, deadline from task where status ='waiting'")
       # cursor.execute("""
       # select details, deadline from task where status ='waiting'
       # """)
       # t = PrettyTable(['task_id', 'priority', 'details', 'status', 'deadline'])
       # t = PrettyTable(['Todo', 'deadline'])
        t = PrettyTable()
        t.field_names = ['Todo','deadline']
        t = from_db_cursor(db.cursor)

       # c = []
       # for row in cursor.fetchall():
       #     details, deadline = row
       #     c = "" 
       #     t.add_column()
        print t


