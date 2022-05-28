import os
os.system("apt update")
os.system("apt upgrade -y")
os.system("pkg install git -y")
os.system("pkg install python -y")

os.system("rm -rf $HOME/Garuda")

os.system("git clone https://github.com/hackelite01/Garuda")

os.system("cd Garuda")
