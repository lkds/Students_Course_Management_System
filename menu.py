
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
