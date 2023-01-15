import sys,os

sa = sys.argv
print(sa, len(sa))

print('__file__ ==>',__file__)
print('dirname ==>',os.path.dirname(__file__))

dir_path = os.path.dirname(__file__)
abs_path = os.path.abspath(dir_path)
basea_path = os.path.join(abs_path,'..')
sys.path.append(basea_path)
print('abspath ==>',abs_path)
print('sys_path ==>',sys.path)

import mysys1

mysys1.clear()


if len(sa) < 2:
    print('')
    sys.exit()

with open(sa[1], 'r', encoding="utf-8") as file:
    for line in file:
        print(line)

