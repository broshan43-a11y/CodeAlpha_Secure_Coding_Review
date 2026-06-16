import sqlite3
import hashlib

username = input("Username: ")
password = input("Password: ")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM users WHERE username=? AND password=?",
    (username, hashed_password)
)

result = cursor.fetchone()

if result:
    print("Login Successful")
else:
    print("Invalid Credentials")

conn.close()