import sqlite3, os.path
from Student import Student

dir_path = os.path.dirname(__file__)
BASE_CAMP = os.path.dirname(dir_path)
high_camp = os.path.abspath(BASE_CAMP)
student_path = os.path.join(high_camp,'student.csv')

students = []
with open('student.csv', 'r', encoding= 'utf-8') as file:
    students = [Student(line.strip()) for i, line in enumerate(file) if i != 0]

students_tuble = []
for i in students:
    students_tuble.append(i.to_tuple())

BASE_CAMP = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_CAMP,'exam.db')

# exit()
conn = sqlite3.connect(db_path)
def insert_data():
    with conn:
        cur = conn.cursor()
        sql = "insert into Student (name, gender, age, grade, addr) values (?, ?, ?, ?, ?)"
        cur.executemany(sql, students_tuble)

        conn.commit()

def select_data():
    with conn:
        cur = conn.cursor()
        sql = """select name, gender, age, grade, addr 
                    from Student order by substr(grade, 1 ,1), grade desc"""
        cur.execute(sql)
        rows = cur.fetchall()
        for row in  rows:
            print(row)

select_data()