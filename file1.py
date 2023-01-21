def write_file():
    with open("student.csv", "w", encoding="utf8") as file:
        file.write("이름,성별,나이,성적,주소\n")
        file.write("김일수,남,23,80,서울시 노원구 중계동 123-45번지\n")
        file.write("홍길순,여,25,75,부산시 동래구 동래1동 45-7번지\n")
        file.write("강대성,남,45,55,인천광역시 영구 을미동 777번지\n")
        file.write("최승리,남,34,90,부산직할시 북구 만덕동 333-9번지\n")
        file.write("강감찬,남,90,100,부산시 부구 덕천동 45번\n")
        file.write("갑돌이,남,38,65,강원도 속초시 중구 토성동 888번지\n")
        file.write("박삼순,여,31,70,대전시 남구 대밭동 438번지\n")
        file.write("김갑순,여,28,85,진주시 남구 논개동 111번지\n")
        file.write("이갑순,여,28,85,전라북도 전주시 맛구 비빔동 777번\n")
        file.write("이순신,남,88,89,포항시 바다구 물회동 898")

def read_file():
    with open("student.csv","r", encoding="utf8") as file:
        for line in file:
            print("line>>>",line)

write_file()
read_file()