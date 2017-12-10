import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully");

print('1')
cur = conn.cursor()
cur.execute("SELECT * FROM file_list")
 
rows = cur.fetchall()
print('2') 
for row in rows:
    print('3')
    print(row)
