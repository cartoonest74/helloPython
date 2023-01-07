from functools import reduce

int_numbers = [1,2,3,4]

re_ob = reduce(lambda x,y : x*y, int_numbers)
print(type(re_ob))