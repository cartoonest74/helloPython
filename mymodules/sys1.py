import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(mysys))))

from .. import mysys
mysys.clear()

argv = sys.argv
print("sys argv>> ",argv, len(argv))

if len(argv) < 2:
    sys.exit()

with open(argv[1], "r", encoding="utf-8") as file:
    for line in file:
        print(line)
 