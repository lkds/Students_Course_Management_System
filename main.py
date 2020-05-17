'''
@Descripttion: 
@version: 
@Author: Paul
@Date: 2020-05-16 17:54:56
@LastEditors: Paul
@LastEditTime: 2020-05-16 22:10:43
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
<q>     退出
<h>     帮助""")


def showHelp():
    print("""
        牛叉的学生管理系统
    """)
    modules.addNewCourse('数据库', 1, 1)


def mainLoop():
    drawMenu()
    while(True):
        cmd = input()
        if (cmd == '1'):
            menu.studentMenuLoop()
        elif (cmd == '2'):
            pass
        elif (cmd == '3'):
            menu.courseMenuLoop()
        elif(cmd == '4'):
            menu.collegeMenuLoop()
        elif(cmd == 'h'):
            showHelp()
        elif (cmd == 'q'):
            os._exit(0)


if __name__ == '__main__':
    mainLoop()
