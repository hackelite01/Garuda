import os
os.system('clear')
os.system('sh requirement.sh')
os.system('rm requirement.sh')
os.system('rm -rf __pycache__')
exec(open('/data/data/com.termux/files/home/Garuda/lg.py','r').read())
