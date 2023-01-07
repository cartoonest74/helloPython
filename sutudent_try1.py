g_grade = ['A','B','C','D','F']
g_grade.reverse()

# 이름 성 제외하고  '*' 처리
def create_blind(names):
    blind_name = map(lambda x:x if names.index(x) ==0 else '*',names)
    return ''.join(list(blind_name))
class School:
    grade = ''
    count = 0
    score_total = 0
    def __init__(self,line):
        name, gender, age, score = line.split(',')
        self.name= name
        self.gender = gender
        self.age = age
        self.score = int(score)
        School.score_total += self.score
        School.count += 1
    def __str__(self):
        blind_name = create_blind(self.name)
        return '{}**\t{}\t{}\t{}'.format(self.name[0], self.gender, self.age, self.grade)
    
    # 성적 => 학점 변환
    def change_grade(self):
        score_v = self.score // 10
        if score_v == 10: 
            self.grade = 'A+'
        else:
            self.grade = g_grade[score_v - 5]

students = []
def file_read(read_csv):
    with open(read_csv,'r',encoding='utf8') as file:
        students = [School(line.strip()) for i,line in enumerate(file) if i !=0]
        return students

#file1.py 에서 저장한 student.csv
students_list = file_read('student.csv')
students_list.sort(key = lambda stu:stu.score,reverse=True)
grade_m = map(lambda stu: stu.change_grade(), students_list)
list(grade_m)

from functools import reduce
#총점 / 평균
total_stu = reduce(lambda x,y:(x if type(x) == int else x.score) + y.score,students_list)
average_stu = round(total_stu/School.count,2)
print('종합점수: {}, 평균점수: {}'.format(total_stu, average_stu ))

# 평균 이상인 학생 이름,성적 출력
high_stu = filter(lambda x:x.score >= average_stu, students_list) 
print('이름\t성별\t나이\t학점')
print('---\t---\t---\t---')
for sx in high_stu:
    print(sx.name, sx.score)

# 전체 학생 이름, 성별, 나이, 학점 출력
print('이름\t성별\t나이\t학점')
print('---\t---\t---\t---')
for s in students_list:
    # if s.score >= average_stu:
    print(s)
# print(School.score_total)