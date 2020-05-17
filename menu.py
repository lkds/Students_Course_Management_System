
from modules import *

########################通用函数###########################


def printHeader(data):
    """
    打印表头
    """
    header = dict()
    header['studentID'] = '学生ID'
    header['departmentID'] = '学院ID'
    header['name'] = '姓名'
    header['studentNumber'] = '学号'
    header['gender'] = '性别'
    header['grade'] = '年级'
    header['birthday'] = '生日'
    header['scID'] = '选课ID'
    header['courseID'] = '课程ID'
    header['grades'] = '成绩'
    header['teacherID'] = '教师ID'
    header['courseName'] = '课程名'
    for k in data.keys():
        print(header[k], '\t', end='')
    print('')


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

########################学生管理###########################


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
        if(selectCourseByID(studentID, int(courseID))):
            print("成功选取课程", courseID)
        else:
            print("操作失败！")
    else:
        print("课程输入错误！")


def getSelectedCourse(studentID):
    course = getStudentAllCourse(studentID)
    if(course):
        printHeader(course[0])
        printTable(course)
    else:
        print("无记录！")


def quitSelectedCourse(studentID):
    getSelectedCourse(studentID)
    print('请输入退选课程ID：', end='')
    courseID = int(input())
    if (getCourseByID(courseID)):
        if(getStudentSelectedCourseByCourseID(studentID, courseID)):
            if (quitCourseByCourseID(studentID, courseID)):
                print('退课成功！')
            else:
                print('退课失败！')
        else:
            print('未选该课程！')
    else:
        print('课程不存在！')


def getSelectedCourseGrade(studentID):
    """
    显示学生已选课程成绩（如果有）
    """
    grade = getStudentGrade(studentID)
    if (grade):
        printHeader(grade[grade.keys[0]])
        printTable(grade)
    else:
        print("暂无成绩！")


def studentMenuLoop():
    print("请输入学生学号：", end='')
    student = getStudentByID(input())
    if (student == None):
        print("未找到相关学生！")
        return
    printHeader(student)
    printTable([student])
    renderStudentMenu()
    studentID = student['studentID']
    while (True):
        cmd = input()
        if (cmd == '1'):
            selectCourse(studentID)
        elif (cmd == '2'):
            getSelectedCourse(studentID)
        elif (cmd == '3'):
            quitSelectedCourse(studentID)
        elif (cmd == '4'):
            getSelectedCourseGrade(studentID)
        elif (cmd == 'q'):
            break
        else:
            continue

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
        cmd = input("请输入菜单项：")
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
        cmd = input("请输入菜单项：")
        if (cmd == '1'):
            printTable([college])
        elif (cmd == '2'):
            getDepartmentTeacher(college['departmentName'])
        elif (cmd == '3'):
            getDepartmentStudent(college['departmentName'])
        elif (cmd == '4'):
            getDepartmentCourse(college['departmentName'])
        elif (cmd == 'q'):
            return


def printKeys(items):
    '''打印输入设置字段值
    '''
    for item in items:
        for key in item.keys():
            item[key] = input("请为{}输入值".format(key))


def collegeModifyMenu(college):
    '''
        学院修改
    '''
    print("/主菜单/学院管理/学院修改管理")
    printCollegeModifyMenu()
    while (True):
        cmd = input("请输入菜单项：")
        if (cmd == '1'):
            for key in college:
                college[key] = input("请为{}输入修改后的值".format(key))
            printKeys(college)
            modifyDepartmentInfo(college)
            print("修改成功")
        # 添加学生
        elif (cmd == '2'):
            # 通过查找一个学生获取其keys
            studentID = 1
            student = getStudentByID(studentID)
            printKeys
            modifyDepartmentInfo(college)
            print("添加成功成功")
        # 添加老师
        elif (cmd == '3'):
             # 通过查找一个老师获取其keys
            teacherID = 1
            teacher = getTeacherByID(teacherID)
            printKeys
            addTeacher(teacher)
        # 开除学生
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
        # 开除老师
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
