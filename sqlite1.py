import sqlite3, os.path
import random

first_names = list("김이박최강고윤엄한배성백전황서천방지마피")
last_names =list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")

def make_name():
    first_name = random.choice(first_names)
    last_name = "".join(random.sample(last_names,2))
    return (first_name + last_name,)

names = []
for i in range(0,100):
    names.append(make_name())

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path  = os.path.join(BASE_DIR, 'test.db')
conn = sqlite3.connect(db_path)
with conn:
    cur = conn.cursor()
    insert_sql = "insert into Student (name) values (?)"
    cur.execute(insert_sql, names)
    
    conn.commit()