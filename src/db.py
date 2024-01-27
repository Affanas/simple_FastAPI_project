#from typing import Union
#from pydantic import BaseModel
from time import sleep
import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
login TEXT NOT NULL,
time_total INTEGER,
total INTEGER,
token INTEGER,
)
''')





