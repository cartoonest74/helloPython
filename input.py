cmd = input("input(usage:이름,나이,성별)>>> ")
print(cmd)

cmds = cmd.split(',')
for key,evaluate in enumerate(cmds) :
    print(evaluate)