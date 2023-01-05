class Casting:
    def to_int(x):
            if type(x) == str:
                x = int(x.strip())
            else:
                x
            return x

class SQUARE:
    def __init__(self):
        print("사각형 created")
    def input_data(self, msg):
        datum = input(msg)
        data = datum.split(',')
        return Casting.to_int(data[0]), Casting.to_int(data[1])

    def rectangle(self, x, y):
        return Casting.to_int(x) * Casting.to_int(y)

    def parallelogram(self, x, y):
        return Casting.to_int(x) * Casting.to_int(y)

while True:
    rect_type = input("사각형의 종류는 ?\n 1) 직사각형\n 2) 평행사변형\n >> (quit:q)")
    if rect_type == 'q':
        break
    if rect_type == '1':
        rect1 = SQUARE()
        # wh = input('가로와 세로는??')
        # x, y = wh.split(',')
        # print("2222>>",x,y)
        x, y= rect1.input_data('가로와 세로는??')
        result = rect1.rectangle(x, y)
        print(f"직사각형의 넓이는 {result}입니다.")
    else:
        rect2 = SQUARE()
        # bh = input('밑변와 높이는??')
        # x, y = bh.split(',')
        x, y= rect1.input_data('밑변와 높이는??')
        result = rect2.parallelogram(x,y)
        print(f"평행사변형의 넓이는 {result}입니다.")
        