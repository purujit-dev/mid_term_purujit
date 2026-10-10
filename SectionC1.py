from fastapi import FastAPI
import sqlite3

conn = sqlite3.connect('library.db')

cursor = conn.cursor()

cursor.execute( 
    'DROP TABLE IF EXISTS books'
)

cursor.execute("""
    CREATE TABLE books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT,
        price REAL
    )


""")

book_data = [('Python Basics','Rao',250),('Sql Guide','Metha',180),('Web dev','Khan',400)]

cursor.executemany("INSERT INTO books (title,author,price) VALUES (?,?,?)",book_data)

cursor.execute("DELETE FROM books WHERE price < 200")

conn.commit()
conn.close()