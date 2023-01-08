g_grade = ['A', 'B', 'C', 'D', 'F']
g_grade.reverse()

class School:
    grade = ''
    total = 0
    count = 0
    average = 0
    sco_gra = ''
    def __init__(self, line):
        name, gender, age, score = line.split(',')
        self.name = name
        self.gender = gender
        self.age = age
        self.score = int(score)
        School.total += self.score 
        School.count += 1
        School.average = round(School.total / School.count , 2)
    def __str__(self):
        if School.sco_gra == 'score':
            return '{}**\t{}\t{}\t{}'.format(self.name[0], self.gender, self.age, self.score)
        else:
            return '{}**\t{}\t{}\t{}'.format(self.name[0], self.gender, self.age, self.grade)

    # 성적 => 학점 변환
    def make_grade(self):
        score_share = self.score // 10 
        if score_share == 10:
            self.grade = 'A+'
        else:
            self.grade = g_grade[score_share -5]

#file1.py 에서 저장한 student.csv
def read_file(file_name):
    students = []
    with open(file_name,'r',encoding='utf8') as file:
        students = [School(line.strip()) for i, line in enumerate(file) if i != 0]
        return students

students = read_file('student.csv')
students.sort(key = lambda stu:stu.score, reverse=True)
grade_list = filter(lambda stu:stu.make_grade(),students)
list(grade_list)

def print_student(loop_list, sco_gra):
    if sco_gra == "score":
        print('\n이름\t성별\t나이\t{}'.format("점수"))
    else:
        print('\n이름\t성별\t나이\t{}'.format("학점"))
    print('---\t---\t---\t---')
    School.sco_gra = sco_gra
    for stu  in loop_list:
        print(stu)

# 전체 학생 이름, 성별, 나이, 학점 출력
print_student(students, 'grade')

from functools import reduce
total_stu = reduce(lambda x,y:(x if type(x) == int else x.score) + y.score, students)

sky_stu = filter(lambda h_stu:h_stu.score >= School.average, students)

# 평균 이상인 학생 이름,성적 출력
print_student(sky_stu, 'score')

#총점 / 평균
print('총점 {}\t평균{}\t'.format(total_stu,School.average))
