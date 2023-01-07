class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    
    def __str__(self):
        return "{}:{}".format(self.name, self.score)

students = [
    Student("GD",88),
    Student("TOP",90),
    Student("DLITE",70)
]

def print_sutdents():
    print('---------------')
    for st in students:
        print(st)

print(students[0])

students = sorted(students, key=lambda stu: stu.score) #내장함수
print_sutdents()

students.sort(key=lambda stu: stu.score) #list sort 함수
print_sutdents()