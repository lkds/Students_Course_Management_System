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


def renderCourseMenu():
    print('''
<1>     查询课程
<2>     删除课程
<3>     修改课程信息
<4>     添加课程
<q>     返回上级菜单
    ''')

def courseMenuLoop():
    
