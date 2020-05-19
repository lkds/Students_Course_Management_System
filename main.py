

import modules
import menu
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
    nav = ['主菜单']
    while (True):
        drawMenu()
        cmd = input()
        if (cmd == '1'):
            menu.studentMenuLoop(nav)
        elif (cmd == '2'):
            menu.teacherMenuLoop(nav)
        elif (cmd == '3'):
            menu.courseMenuLoop(nav)
        elif(cmd == '4'):
            menu.collegeMenuLoop(nav)
        elif(cmd == 'h'):
            showHelp()
        elif (cmd == 'q'):
            os._exit(0)


if __name__ == '__main__':
    mainLoop()
