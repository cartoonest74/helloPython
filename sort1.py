numbers = [5,4,3,2,1]
sort_numbers = sorted(numbers) # reversed(numbers)
print("sort_numbers => ", sort_numbers)
print("numbers => ", numbers)

numbers.sort() # 리스트 주소에 접근
print("asc>>", numbers)

numbers.sort(reverse=True)
print("desc>>", numbers)