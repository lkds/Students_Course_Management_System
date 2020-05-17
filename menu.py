
from modules import *

########################通用函数###########################


def printTable(data):
    """
    打印一组数据
    :data:list
    :data[0]:dict
    """
    for item in data:
        for key in item.keys():
            print(item[key], '\t', end='')
        print('')


def renderStudentMenu():
    print('''
<1>     选课
<2>     查询已选课程
<3>     退课
<4>     查询成绩
<q>     返回上级菜单
    ''')


def selectCourse(studentID):
    """
    选课功能
    """
    course = getCourse()
    print("课程编号\t学院\t老师\t名称")
    printTable(course)
    print('请输入课程编号：\t', end='')
    courseID = input()
    if(getCourseByID(courseID)):
        selectCourseByID(studentID, courseID)
        print("成功选取课程", courseID)
    else:
        print("课程输入错误！")


def studentMenuLoop():
    print("请输入学生学号：", end='')
    student = getStudentByID(input())
    if (student == None):
        print("未找到相关学生！")
        return
    renderStudentMenu()
    while (True):
        cmd = input()
        if (cmd == '1'):
            selectCourse(student)

########################课程管理###########################
def renderCourseMenu():
    print('''
<1>     查询课程
<2>     删除课程
<3>     修改课程信息
<4>     添加课程
<q>     返回上级菜单
    ''')

def printCourseSearchMenu():
    print('''
<1>     查询全部
<2>     按课程id查询
<3>     按课程名称查询
<4>     按任课老师id查询
<5>     按任课老师姓名查询
<q>     返回上级菜单
    ''')

def printCourseDeleteMenu():
    print('''
<1>     按课程id删除
<2>     按课程名称删除
<q>     返回上级菜单
    ''')

def courseSearchMenu():
    '''
        查询课程
    '''
    print("/主菜单/课程管理/查询课程")
    printCourseSearchMenu()
    while (True):
        print("请输入菜单项：", end='')
        cmd = input()
        if (cmd == '1'):#查询全部
            course = getCourse()
            printTable(course)         
        elif (cmd == '2'):#按课程id查询
            print("请输入需要查询的课程id:",end='')
            course = getCourseByID(input())
            printTable(course)
        elif (cmd == '3'):#按课程名称查询
            print("请输入需要查询的课程的名称:",end='')
            course = getCourseByName(input())
            printTable(course)
        elif (cmd == '4'):#按任课老师id查询
            print("请输入需要查询的课程的任课老师id:",end='')
            course = getCoursebyTeacherID(input())
            printTable(course)
        elif (cmd == '5'):#按照任课老师姓名查询
            print("请输入需要查询的课程的任课老师姓名:",end='')
            course = getCoursebyTeacherName(input())
            printTable(course)
        elif (cmd == '6'):#按照学分查询
            print("请输入课程学分:",end='')
            course= getCoursebycourseCredit(input())
            printTable(course)
        elif (cmd == 'q'):
            return

def courseDeleteMenu():
    '''
        删除课程
    '''
    print("/主菜单/课程管理/删除课程")
    printCourseDeleteMenu()
    while(True):
        print("请输入菜单项:",end='')
        cmd = input()
        if(cmd == '1'):#按照课程id删除课程
            print("请输入需要查询的课程的id:",end='')
            courseID=input()
            course = getCourseByID(courseID)
            if(len(course)==0):
                print("不存在该课程")
            else:
                delCourseByID(courseID)
                quitCourseBycourseID(courseID)#同时删除学生的选课记录
        elif (cmd == '2'):#按课程名称删除课程
            print("请输入需要查询的课程的任课老师姓名:",end='')
            courseName = input()
            course = getCourseByName(courseName)
            if(len(course)==0):
                print("不存在该课程")
            else:
                delCourseByName(courseName)
                quitCourseBycourseName(courseName)#同时删除学生的选课记录      
        elif (cmd == 'q'):
            return
        

def courseModifyMenu():
    '''
        修改课程信息
    '''
    print("/主菜单/课程管理/修改课程信息:")
    courseID = input("请输入需要修改的课程id:")   
    if(len(getCourseByID(courseID))==0):
        print("抱歉，并未找到该课程")
    else:
        courseName = input("请输入更新后的课程名称:")
        if(len(getCourseByName(courseName))!=0):
            print("抱歉已有叫该名称的课程")
        else:
            teacherID = input("请输入更新后的任课教师id:")
            if(len(getTeacherByID(teacherID))==0):
                print("抱歉不存在该教师")
            else:
                departmentID = input("请输入更新后的课程所属学院:")
                if(len(getDepartmentId(departmentID))==0):
                    print("抱歉不存在该学院")
                else:
                    courseCredit = input("请输入更新后的课程学分:")
                    updateCourse(courseID, courseName, departmentID, teacherID,courseCredit)

def courseAddMenu():
    '''
    添加课程
    '''
    print("/主菜单/课程管理/添加课程:")
    while(True):
        courseName = input("请输入课程名称:")
        if(len(getCourseByName(courseName))!=0):
            print("抱歉已有叫该名称的课程,请重新输入")
        else：
            break
    while(True):
        teacherID = input("请输入该课程的任课教师id:")
        if(len(getTeacherByID(teacherID))==0):
            print("抱歉不存在该教师,请重新输入")
        else:
            break
    while(True):
        departmentID = input("请输入该课程所属学院:")
        if(len(getDepartmentId(departmentID))==0):
            print("抱歉不存在该学院")
        else:
            break
    while(True):     
        courseCredit = input("请输入课程学分:")
        addNewCourse(courseName, departmentID, teacherID,courseCredit)





def courseMenuLoop():
    '''
        课程管理
    '''
    print("/主菜单/课程管理")
    renderCourseMenu()
    while (True):
        print("请输入菜单项：", end='')
        cmd = input()
        if (cmd == '1'):#查询课程
            courseSearchMenu()
        elif (cmd == '2'):#删除课程
            courseDeleteMenu()
        elif (cmd == '3'):#修改课程信息
            courseModifyMenu()
        elif (cmd == '4'):#添加课程
            courseAddMenu()
        elif (cmd == 'q'):
            return

    
########################学院管理###########################

def printCollegeSearchMenu():
    print('''
<1>     查询学院信息
<2>     查询学院所有老师
<3>     查询学院所有学生
<4>     查询学院所有课程
<q>     返回上级菜单
    ''')


def printCollegeModifyMenu():
    print('''
<1>     查询学院所有课程
<2>     添加学生
<3>     添加老师
<4>     开除学生
<5>     解雇老师
<q>     返回上级菜单
    ''')


def collegeMenuLoop():
    '''
        学院管理菜单
    '''
    print("/主菜单/学院管理")
    print("请输入学院：", end='')
    college = getDepartmentInfoByName(input())
    if (college == None):
        print("不存在该学院！")
        return

    print('''
<1>     查询操作
<2>     更改操作
<q>     返回上级菜单
     '''
          )
    while (True):
        cmd = input("请输入菜单项：", end='')
        if (cmd == '1'):
            collegeSearchMenu(college)
        if (cmd == '2'):
            collegeModifyMenu(college)
        elif (cmd == 'q'):
            return


def collegeSearchMenu(college):
    '''
        学院查询
    '''
    print("/主菜单/学院管理/学院查询管理")
    printCollegeSearchMenu()
    while (True):
        cmd = input("请输入菜单项：", end='')
        if (cmd == '1'):
            printTable(college)
        elif (cmd == '2'):
            getDepartmentTeacher(college['departmentName'])
        elif (cmd == '3'):
            getDepartmentStudent(college['departmentName'])
        elif (cmd == '4'):
            getDepartmentCourse(college['departmentName'])
        elif (cmd == 'q'):
            return


def collegeModifyMenu(college):
    '''
        学院修改
    '''
    print("/主菜单/学院管理/学院修改管理")
    printCollegeModifyMenu()
    while (True):
        cmd = input("请输入菜单项：", end='')
        if (cmd == '1'):
            for key in college:
                college[key] = input("请为{}输入修改后的值".format(key), end='')
            modifyDepartmentInfo(college)
            print("修改成功")

        elif (cmd == '2'):
            getDepartmentTeacher()
        elif (cmd == '3'):
            getDepartmentTeacher()
        elif (cmd == '4'):
            while (True):
                print("请输入学生ID：", end='')
                student = getStudentByID(input())
                if (college == None):
                    print("不存在该学生！")
                else:
                    deleteStudent(student['studentID'])
                    print("开除成功")
                    break
        elif (cmd == '5'):
            while (True):
                print("请输入老师ID：", end='')
                teacher = getTeacherByID(input())
                if (teacher == None):
                    print("不存在该老师！")
                else:
                    deleteTeacher(teacher['teacherID'])
                    print("解雇成功")
                    break
        elif (cmd == 'q'):
            return
