# def var_param(a, *vp):
#     print(type(vp))
#     print(a, len(vp), vp[len(vp)-1])

# var_param('AA', 'bbb', 'ccc')

# def default_param(a, b='BBB'):
#     print(a, b)

# default_param('AAA')

#plus
import re

def plus(a,b):
    return a + b

#minus
def minus(a,b):
    return a - b

#division
def division(a,b):
    float_value = a / b
    return round(float_value,3)

#multifle
def multifle(a,b):
    return a * b

cmd  = input('input(usage:1 + 1 (+,-,/,* pick 1) >>>')
cmds = cmd.split(' ')
error_msg = '양식에 맞게 다시 입력해주세요!'
cal_regex = re.compile("[a-zA-Z]")
if len(cmds) != 3:
    print(error_msg)
    exit()
elif cal_regex.search(''.join(cmds)):
    print(error_msg)
    exit()
else:
     float_a = float(cmds[0])
     float_c = float(cmds[2])

def cal(a,v,c):
    out_value = 0
    math_tool = ['+','/','*','-']
    if v not in math_tool:
        print(error_msg)
        return exit()
    elif v == '+':
        out_value = plus(a,c)
    elif v == '-':
        out_value = minus(a,c)
    elif v == '/':
        out_value = division(a,c)
        return print(int(str(out_value).split('.')[0])) if int(str(out_value).split('.')[1]) == 0 else print(out_value)  
    else:
        out_value = multifle(a,c)

    return print(out_value) 

cal(float_a,cmds[1],float_c)