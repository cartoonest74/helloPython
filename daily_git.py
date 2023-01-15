import os, sys
import datetime

argv = sys.argv
date_now = datetime.datetime.now()
default_msg = '{}'.format(date_now.strftime(''))
commit_msg = default_msg
has_msg = len(argv) >= 2

print(commit_msg)

if has_msg:
    commit_msg = argv[1]
else:
    inp_msg = input("default msg right?(yes: Enter or input message >>)")
    if inp_msg != '':
        commit_msg = inp_msg

os.system('git add --all')
os.system('git commit -am {}'.format(commit_msg))
os.system('git push')
