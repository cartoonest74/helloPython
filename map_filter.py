int_numbers = range(-5,6)
fi_ob = filter(lambda x: x*2, int_numbers)
ma_ob = map(lambda x:x*2, int_numbers)

print('filter => ',list(fi_ob))
print('map => ',list(ma_ob))