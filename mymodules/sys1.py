import sys, os

print(sys.argv, len(sys.argv))

dir_name = os.path.dirname(__file__)
abs_path = os.path.abspath(dir_name)
hello_path = os.path.join(abs_path, '..')
sys.path.append(hello_path) 
print('dir_name >> ', dir_name)
print('abs_path >> ', abs_path)
print('sys_path >>',hello_path)

# clear module
import mysys1
mysys1.clear()

# argv 변수 
sa = sys.argv
if len(sa) < 2:
    sys.exit()

with open(sa[1], "r", encoding="utf-8") as file:
    for line in file:
        print(line)
 