import sys

print(sys.argv, len(sys.argv))

sa = sys.argv
if len(sa) < 2:
    sys.exit()

with open(argv[1], "r", encoding="utf-8") as file:
    for line in file:
        print(line)
 