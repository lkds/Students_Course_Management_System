import modules
import os


def drawMenu():
    print(""" _______   _   __          _    
|_   __ \ (_) [  |        / |_  
  | |__) |__   | |  .--. `| |-' 
  |  ___/[  |  | |/ .'`\ \| |   
 _| |_    | |  | || \__. || |,  
|_____|  [___][___]'.__.' \__/  
""")
    print("""Pilot学生-课程管理系统
<1>     学生课程管理
<2>     教师课程管理
<3>     课程管理
<4>     学院课程管理
<q>     退出
<h>     帮助""")


def showHelp():
    print("""
        牛叉的学生管理系统
    """)


def mainLoop():
    drawMenu()
    while(True):
        cmd = input()
        if (cmd == 1):
            pass
        elif (cmd == 2):
            pass
        elif (cmd == 3):
            pass
        elif(cmd == 4):
            pass
        elif(cmd == 'h'):
            showHelp()
        elif (cmd == 'q'):
            os._exit(0)


if __name__ == '__main__':
    mainLoop()
