import sqlite3

db = sqlite3.connect("main_database.db")

cursor = db.cursor()

cursor.execute("""CREATE TABLE users (
id INTEGER PRIMARY KEY,
username VARCHAR(50),
password_hash VARCHAR(255),
role VARCHAR(50),
created_at DATE
)""")

cursor.execute("""CREATE TABLE genres (
id INTEGER PRIMARY KEY,
name VARCHAR(100)
)""")

cursor.execute("""CREATE TABLE authors (
id INTEGER PRIMARY KEY,
full_name VARCHAR(255)
)""")

cursor.execute("""CREATE TABLE interests (
id INTEGER PRIMARY KEY,
name VARCHAR(100)
)""")

cursor.execute("""CREATE TABLE books (
id INTEGER PRIMARY KEY,
title VARCHAR(500),
description TEXT,
publication_year INTEGER,
cover_path VARCHAR(550),
is_active BOOLEAN
)""")

db.commit()
db.close()