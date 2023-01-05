class Casting:
    def to_into(x):
        if type(x) == str:
            x = int(x.strip())
        else:
            x
        return x

class Square:
    name = "사각형"
    msg = "사각형 가로,세로를 입력해주세요 (usage:가로,세로) >"
    
    def __init__(self):
        print("사각형 생성")
    
    def input_data(self):
        datum = input(self.msg)
        data = datum.split(',') 
        x = Casting.to_into(data[0])
        if len(data) == 0:
            y = x
        else:
            y = Casting.to_into(data[1])
        self.area(x,y)
    def area(self,x,y):
        result = x * y
        return print("{}의 넓이는 {} 입니다.".format(self.name, result))

class Rectangle(Square):
    name = "직사각형"
    msg = "직사각형의 가로,세로를 입력해주세요 (usage:가로,세로) >"
class parallelogram(Square):
    name = "평행사변형"
    msg = "평행사변형의 밑변,높이를 입력해주세요 (usage:밑변,높이) >"
class Foursquare(Square):
    name = "정사각형"
    msg = "정사각형 한변의 길이를 입력해주세요 (usage:한변) >"

rect_all = [Square(), Rectangle(), parallelogram(), Foursquare()]
first_list = [f'{count}) {i.name}' for count,i in enumerate(rect_all) if count != 0]
first_list.insert(0,'사각형의 종류는 ?')
first_list.append('(quit:q) >>')
first_msg = '\n'.join(first_list)

while True:
    rect_index = input(first_msg)
    print('\n+++++++++++++++++++++++++++++++++++++++++')
    if rect_index == 'q':
        break; 
    if Casting.to_into(rect_index) >= len(rect_all):
        rect_index = 0
    rect_type = rect_all[Casting.to_into(rect_index)]
    rect_type.input_data()
