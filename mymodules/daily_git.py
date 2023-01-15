import os, sys
import datetime

now = datetime.datetime.now()
argv_msg = sys.argv
commit_msg = '{}'.format(now.strftime('%Y-%m-%d'))
has_msg = len(argv_msg) >= 2

if has_msg:
    commit_msg = argv_msg[1]

if has_msg == False:
    input_msg = input("Default Message?? (Yes: Enter or input Message >>> ")
    if input_msg != "":
        commit_msg = input_msg

print(commit_msg)
os.system('git add --all')
os.system('git commit -am {}'.format(commit_msg))
os.system('git push')