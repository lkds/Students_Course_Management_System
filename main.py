'''
@Descripttion: 
@version: 
@Author: Paul
@Date: 2020-05-16 17:54:56
@LastEditors: Paul
@LastEditTime: 2020-06-07 11:35:47
'''


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
<h>     帮助
<q>     退出""")


def showHelp():
    print("""
        Pilot的学生管理系统
        Ver.0.0.3alpha
        copyright@Team Pilot
    """)


def mainLoop():
    nav = ['主菜单']
    while (True):
        drawMenu()
        cmd = input('请输入命令：')
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
            print('\nBye~')
            os._exit(0)


if __name__ == '__main__':
    try:
        mainLoop()
    except KeyboardInterrupt:
        print('\nBye~')
