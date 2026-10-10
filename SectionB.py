import sqlite3 

conn = sqlite3.connect("college.db")

cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS students')

cursor.execute("""
    CREATE TABLE students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        course TEXT,
        city TEXT,
        marks REAL
    )


""")

bulk_data = [
    ('Aman','BSc','Jaipur',78),
    ('Priya','BCA','Pali',88),
    ('Rahul','BSc','Jodhpur',45),
    ('Sneha','BSc','Pali',92),
    ('Karan','BCA','Jaipur',30)
]

cursor.executemany("INSERT INTO students (name,course,city,marks) VALUES (?,?,?,?)",bulk_data)

cursor.execute("SELECT name,marks FROM students WHERE marks >= 80")
column = cursor.fetchall()
print(column)

cursor.execute("INSERT INTO students (name,course,city,marks) VALUES (?,?,?,?)",("Vikram","BCA","Udaipur",67))


conn.commit()
conn.close()
