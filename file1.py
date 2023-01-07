def write_file():
    with open("student.csv", "w", encoding="utf8") as file:
        file.write("이름,성별,나이,성적\n")
        file.write("김일수,남,23,80\n")
        file.write("홍길순,여,25,75\n")
        file.write("강대성,남,45,55\n")
        file.write("최승리,남,34,90\n")
        file.write("강감찬,남,90,100\n")
        file.write("갑돌이,남,38,65\n")
        file.write("박삼순,여,31,70\n")
        file.write("김갑순,여,28,85\n")
        file.write("이갑순,여,28,85\n")
        file.write("이순신,남,88,89")

def read_file():
    with open("student.csv","r", encoding="utf8") as file:
        for line in file:
            print("line>>>",line)

write_file()
read_file()