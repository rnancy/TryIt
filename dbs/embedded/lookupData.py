import sqlite3
from prettytable import PrettyTable


db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        select id, priority, details, status, deadline from task where project = 'pymotw'
        """)
        t = PrettyTable(['task_id', 'priority', 'details', 'status', 'deadline'])
        for row in cursor.fetchall():
            task_id, priority, details, status, deadline = row
            t.add_row(row)
            print '%2d {%d} %-20s [%-8s] (%s)' % (task_id, priority, details, status, deadline)
            
        print t


