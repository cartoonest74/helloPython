import re

rex = re.compile('[ㄱ-힣]+구 [ㄱ-힣|0-9]+동')
grade_list = ['A', 'B', 'C', 'D', 'F']
grade_list.reverse()

class Student:
    name = ''
    addr = ''
    age = ''
    addr = ''
    score = ''
    def __init__(self, info):
        name, gender, age, score, addr =info.strip().split(',')
        self.name = name
        self.gender = self.to_genderEng(gender)
        self.age = self.change_age(int(age))
        self.score = self.to_grade(int(score))
        self.addr = self.pick_addr(addr)

    def to_genderEng(self, gender):
        if gender == '남':
            return 'M'
        else:
            return 'F'
    
    def change_age(self, age):
        age_ies = age//10 * 10
        return str(age_ies) + '대'
    
    def to_grade(self, change_score):
        if change_score == 100 : 
            return 'A++'
        elif change_score < 50:
            return 'F'
        else:
            return grade_list[change_score//10 - 5]

    def pick_addr(self, full_addr):
        search_addr = re.search(rex, full_addr)
        return search_addr.group()
        
    def __str__(self):
        return '{}**,{},{}대,{},{}'.format(self.name[0], self.gender, self.age, self.score, self.addr)
    
    def to_tuple(self):
        return (self.name[0]+'**' , self.gender, self.age, self.score, self.addr, )
