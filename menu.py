
from modules import *
import datetime
from copy import deepcopy
########################通用函数###########################


def my_align(_string, _length, _type='L'):
    """
    中英文混合字符串对齐函数
    my_align(_string, _length[, _type]) -> str

    :param _string:[str]需要对齐的字符串
    :param _length:[int]对齐长度
    :param _type:[str]对齐方式（'L'：默认，左对齐；'R'：右对齐；'C'或其他：居中对齐）
    :return:[str]输出_string的对齐结果
    """
    _str_len = len(_string)  # 原始字符串长度（汉字算1个长度）
    for _char in _string:  # 判断字符串内汉字的数量，有一个汉字增加一个长度
        if u'\u4e00' <= _char <= u'\u9fa5':  # 判断一个字是否为汉字（这句网上也有说是“ <= u'\u9ffff' ”的）
            _str_len += 1
    _space = _length-_str_len  # 计算需要填充的空格数
    if _type == 'L':  # 根据对齐方式分配空格
        _left = 0
        _right = _space
    elif _type == 'R':
        _left = _space
        _right = 0
    else:
        _left = _space//2
        _right = _space-_left
    return ' '*_left + _string + ' '*_right


def alignPrint(data):
    """
    :data-list
    """
    for item in data:
        print('{}'.format(my_align(str(item), 10, 'C')), end='')
    print('')


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
    header['title'] = '职称'
    header['teacherNumber'] = '教职工号'
    header['office'] = '办公室'
    header['homeAddress'] = '住址'
    header['courseID'] = '课程号'
    header['teacherName'] = '姓名'
    header['courseName'] = '课程名'
    header['courseCredit'] = '学分'
    header['departmentName'] = '学院名'
    header['departmentAddress'] = '学院地址'
    header['contactInformation'] = '联系方式'
    content = []
    for k in data.keys():
        content.append(header[k])
    alignPrint(content)


def printTable(data):
    """
    打印一组数据
    :data:list
    :data[0]:dict
    """
    for item in data:
        for key in item.keys():
            print('{}'.format(my_align(str(item[key]), 10, 'C')), end='')
        print('')
    print('')


def printNav(nav):
    """
    :param nav-[list] 导航数组，['主菜单'，'课程管理','增加课程']
    """
    print('-------------------------', end='')
    print('/', end='')
    print('/'.join(nav), end='')
    print('-------------------------')


def printKeys(item):
    '''
    获取修改值
    :param item=[dict] 原数据
    :return [dict] 新数据
    '''

    for key in item.keys():
        if (key != list(item.keys())[0]):
            print("请为{}输入值(当前：{},回车保持不变)：".format(key, item[key]), end='')
            if (key == 'birthday'):
                print("例：2020-5-14")
            #     item[key] =datetime.datetime.strptime(input(), '%Y-%m-%d')
            # else:
            val = input()
            if(val != ''):
                item[key] = val
    return item
########################学生管理###########################


def renderStudentMenu():
    print('''
<1>     选课
<2>     查询已选课程
<3>     退课
<4>     查询成绩
<q>     返回上级菜单
    ''')


def selectCourse(studentID, nav):
    """
    选课功能
    """
    newNav = deepcopy(nav)
    newNav.append('选课')
    printNav(newNav)
    course = getCourse()
    if (len(course) == 0):
        print("暂无课程")
        return
    printHeader(course[0])
    printTable(course)
    print('请输入课程编号：', end='')
    courseID = input()
    if (courseID == ''):
        return
    if(getCourseByID(courseID)):
        if(selectCourseByID(studentID, int(courseID))):
            print("成功选取课程", courseID)
        else:
            print("操作失败！")
    else:
        print("课程输入错误！")


def getSelectedCourse(studentID, nav=None):
    if (nav):
        newNav = deepcopy(nav)
        newNav.append('选课结果')
        printNav(newNav)
    course = getStudentAllCourse(studentID)
    if(course):
        printHeader(course[0])
        printTable(course)
    else:
        print("无记录！")


def quitSelectedCourse(studentID, nav):
    newNav = deepcopy(nav)
    newNav.append('退课')
    printNav(newNav)
    getSelectedCourse(studentID)
    print('请输入退选课程ID：', end='')
    courseIDStr = input()
    if (courseIDStr == ''):
        print('输入错误！')
        return
    courseID = int(courseIDStr)
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


def calGPA(grade):
    if (grade < 60):
        return 0
    elif (grade >= 90):
        return 4
    else:
        return (grade - 50)/10


def getSelectedCourseGrade(studentID, nav):
    """
    显示学生已选课程成绩（如果有）
    """
    newNav = deepcopy(nav)
    newNav.append('查询成绩')
    printNav(newNav)
    grade = getStudentGrade(studentID)
    if (grade):
        gpa = sum(calGPA(item['grades']) * item['courseCredit']
                  for item in grade) / sum(item['courseCredit'] for item in grade)
        printHeader(grade[0])
        printTable(grade)
        print('GPA:', gpa)
    else:
        print("暂无成绩！")


def studentManageLoop(nav):
    print("请输入学生ID：", end='')
    student = getStudentByID(input())
    if (student == None):
        print("未找到相关学生！")
        return
    printHeader(student[0])
    printTable(student)
    studentID = student[0]['studentID']
    newNav = deepcopy(nav)
    newNav.append(student[0]['name'])
    while (True):
        printNav(newNav)
        renderStudentMenu()
        cmd = input()
        if (cmd == '1'):
            selectCourse(studentID, newNav)
        elif (cmd == '2'):
            getSelectedCourse(studentID, newNav)
        elif (cmd == '3'):
            quitSelectedCourse(studentID, newNav)
        elif (cmd == '4'):
            getSelectedCourseGrade(studentID, newNav)
        elif (cmd == 'q'):
            break
        else:
            print('输入错误，请重试！')
            continue


def studentQuery(t, data, nav):
    if (t == 0):
        student = getStudent()
    elif (t == 1):
        student = getStudentBystudentNumber(data)
    elif (t == 2):
        student = getStudentByName(data)
    newNav = deepcopy(nav)
    newNav.append('查询结果')
    printNav(newNav)
    if (len(student) == 0):
        print('暂无数据')
    else:
        printHeader(student[0])
        printTable(student)


def studentQueryLoop(nav):
    newNav = deepcopy(nav)
    newNav.append('学生查询')
    while (True):
        printNav(newNav)
        print('''
<1>     学生列表
<2>     按学号查询
<3>     按姓名查询
<q>     退出
        ''')
        cmd = input('请输入菜单项:')
        if (cmd == '1'):
            studentQuery(0, 0, newNav)
        elif (cmd == '2'):
            studentNumber = input('请输入学号:')
            studentQuery(1, studentNumber, newNav)
        elif (cmd == '3'):
            studentName = input('请输入姓名:')
            studentQuery(2, studentName, newNav)
        elif (cmd == 'q'):
            break
        else:
            print('输入错误！')


def studentMenuLoop(nav):
    newNav = deepcopy(nav)
    newNav.append('学生菜单')
    while (True):
        printNav(newNav)
        print('''
<1>     学生查询
<2>     学生管理
<q>     返回上级菜单
        ''')
        cmd = input('请输入菜单项')
        if (cmd == '1'):
            studentQueryLoop(newNav)
        elif (cmd == '2'):
            studentManageLoop(newNav)
        elif (cmd == 'q'):
            break
        else:
            print('输入错误！')

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


def courseSearchMenu(nav):
    '''
        查询课程
    '''
    newNav = deepcopy(nav)
    newNav.append('查询课程')
    while (True):
        printNav(newNav)
        printCourseSearchMenu()
        print("请输入菜单项：", end='')
        cmd = input()
        if (cmd == '1'):  # 查询全部
            course = getCourse()
            if (len(course) == 0):
                print('暂无课程')
                continue
            printHeader(course[0])
            printTable(course)
        elif (cmd == '2'):  # 按课程id查询
            print("请输入需要查询的课程id:", end='')
            course = getCourseByID(input())
            if (len(course) == 0):
                print('未找到相关课程')
                continue
            printHeader(course[0])
            printTable(course)
        elif (cmd == '3'):  # 按课程名称查询
            print("请输入需要查询的课程的名称:", end='')
            course = getCourseByName(input())
            if (len(course) == 0):
                print('未找到相关课程')
                continue
            printHeader(course[0])
            printTable(course)
        elif (cmd == '4'):  # 按任课老师id查询
            print("请输入需要查询的课程的任课老师id:", end='')
            course = getCoursebyTeacherID(input())
            if (len(course) == 0):
                print('未找到相关课程')
                continue
            printHeader(course[0])
            printTable(course)
        elif (cmd == '5'):  # 按照任课老师姓名查询
            print("请输入需要查询的课程的任课老师姓名:", end='')
            course = getCoursebyTeacherName(input())
            if (len(course) == 0):
                print('未找到相关课程')
                continue
            printHeader(course[0])
            printTable(course)
        elif (cmd == '6'):  # 按照学分查询
            print("请输入课程学分:", end='')
            course = getCoursebycourseCredit(input())
            if (len(course) == 0):
                print('未找到相关课程')
                continue
            printHeader(course[0])
            printTable(course)
        elif (cmd == 'q'):
            return


def courseDeleteMenu(nav):
    '''
        删除课程
    '''
    newNav = deepcopy(nav)
    newNav.append('删除课程')
    while (True):
        printNav(newNav)
        printCourseDeleteMenu()
        print("请输入菜单项:", end='')
        cmd = input()
        if(cmd == '1'):  # 按照课程id删除课程
            print("请输入需要删除的课程的id:", end='')
            courseID = input()
            course = getCourseByID(courseID)
            if(len(course) == 0):
                print("不存在该课程")
            else:
                # if (delCourseByID(courseID) and quitCourseBycourseID(courseID)):
                #     print('成功删除课程', course[0]['courseName'])  # 同时删除学生的选课记录
                if(delCourseByID(courseID)):
                    print('成功删除课程', course[0]['courseName'])  # 同时删除学生的选课记录
        elif (cmd == '2'):  # 按课程名称删除课程
            print("请输入需要删除的课程的课程名称:", end='')
            courseName = input()
            course = getCourseByName(courseName)
            if(len(course) == 0):
                print("不存在该课程")
            else:
                if(delCourseByName(courseName)):
                    print('成功删除课程', course[0]['courseName'])  # 同时删除学生的选课记录
                # quitCourseBycourseName(courseName)  # 同时删除学生的选课记录
        elif (cmd == 'q'):
            return


def courseModifyMenu(nav):
    '''
        修改课程信息
    '''
    newNav = deepcopy(nav)
    newNav.append('修改课程')
    printNav(newNav)
    courseID = input("请输入需要修改的课程id:")
    course = getCourseByID(courseID)
    if(len(course) == 0):
        print("抱歉，并未找到该课程")
    else:
        newCourse = printKeys(course[0])
        if (updateCourse(newCourse)):
            print('修改成功！')
        else:
            print('操作失败！')


def courseAddMenu(nav):
    '''
    添加课程
    '''
    newNav = deepcopy(nav)
    newNav.append('添加课程')
    printNav(newNav)
    while(True):
        courseName = input("请输入课程名称:")
        if(len(getCourseByName(courseName)) != 0):
            print("抱歉已有叫该名称的课程,请重新输入")
        else:
            break
    while(True):
        teacherID = input("请输入该课程的任课教师id:")
        if(len(getTeacherByID(teacherID)) == 0):
            print("抱歉不存在该教师,请重新输入")
        else:
            break
    while(True):
        departmentID = input("请输入该课程所属学院ID:")
        if(len(getDepartmentById(departmentID)) == 0):
            print("抱歉不存在该学院")
        else:
            break
    while(True):
        courseCredit = input("请输入课程学分:")
        try:
            courseCredit = int(courseCredit)
            break
        except:
            print('输入有误，请重试！')
    addNewCourse(courseName, departmentID, teacherID, courseCredit)


def courseMenuLoop(nav):
    '''
        课程管理
    '''
    newNav = deepcopy(nav)
    newNav.append('课程管理')
    while (True):
        printNav(newNav)
        renderCourseMenu()
        print("请输入菜单项：", end='')
        cmd = input()
        if (cmd == '1'):  # 查询课程
            courseSearchMenu(newNav)
        elif (cmd == '2'):  # 删除课程
            courseDeleteMenu(newNav)
        elif (cmd == '3'):  # 修改课程信息
            courseModifyMenu(newNav)
        elif (cmd == '4'):  # 添加课程
            courseAddMenu(newNav)
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
<1>     修改学院信息
<2>     添加学生
<3>     添加老师
<4>     开除学生
<5>     解雇老师
<q>     返回上级菜单
    ''')


def collegeMenuLoop(nav):
    '''
        学院管理菜单
    '''
    newNav = deepcopy(nav)
    newNav.append('学院管理')
    printNav(newNav)
    colleges = getDepartmentInfo()
    printHeader(colleges[0])
    printTable(colleges)
    print("请输入学院ID：", end='')
    college = getDepartmentById(input())
    if (college == None):
        print("不存在该学院！")
        return

    while (True):
        printNav(newNav)
        print('''
<1>     查询操作
<2>     更改操作
<q>     返回上级菜单
     '''
              )
        cmd = input("请输入菜单项：")
        if (cmd == '1'):
            collegeSearchMenu(college, newNav)
        elif (cmd == '2'):
            collegeModifyMenu(college, newNav)
        elif (cmd == 'q'):
            return


def collegeSearchMenu(college, nav):
    '''
        学院查询
    '''
    newNav = deepcopy(nav)
    newNav.append('查询管理')
    while (True):
        printNav(newNav)
        printCollegeSearchMenu()
        cmd = input("请输入菜单项：")
        depart = college[0]
        deptID = depart['departmentID']
        if (cmd == '1'):
            printHeader(depart)
            printTable(college)
        elif (cmd == '2'):
            teachersInfo = getDepartmentTeacher(deptID)
            printHeader(teachersInfo[0])
            printTable(teachersInfo)
        elif (cmd == '3'):
            studentsInfo = getDepartmentStudent(deptID)
            printHeader(studentsInfo[0])
            printTable(studentsInfo)
        elif (cmd == '4'):
            coursesInfo = getDepartmentCourse(deptID)
            printHeader(coursesInfo[0])
            printTable(coursesInfo)
        elif (cmd == 'q'):
            break


def collegeModifyMenu(college, nav):
    '''
        学院修改
    '''
    newNav = deepcopy(nav)
    newNav.append('学院修改管理')
    while (True):
        printNav(newNav)
        printCollegeModifyMenu()
        cmd = input("请输入菜单项：")
        if (cmd == '1'):
            modifiedCo = printKeys(college[0])
            if (modifyDepartmentInfo(modifiedCo)):
                print('修改成功')
            else:
                print('修改失败')

        # 添加学生
        elif (cmd == '2'):
            # 通过查找一个学生获取其keys
            studentID = 1
            student = getStudentByID(studentID)[0]
            newStudent = printKeys(student)
            if (addStudent(newStudent)):
                print('添加成功')
            else:
                print('添加失败')

        # 添加老师
        elif (cmd == '3'):
            # 通过查找一个老师获取其keys
            teacherID = 1
            teacher = getTeacherByID(teacherID)[0]
            newTeacher = printKeys(teacher)
            if (addTeacher(newTeacher)):
                print('添加成功')
            else:
                print('添加失败')
        # 开除学生
        elif (cmd == '4'):
            while (True):
                print("请输入学生ID：", end='')
                student = getStudentByID(input())[0]
                if (student == None):
                    print("不存在该学生！")
                    break
                else:
                    if (deleteStudent(student['studentID'])):
                        print('删除成功')
                    else:
                        print('删除失败')
                    break
        # 开除老师
        elif (cmd == '5'):
            while (True):
                print("请输入老师ID：", end='')
                teacher = getTeacherByID(input())[0]
                if (teacher == None):
                    print("不存在该老师！")
                    break
                if (deleteTeacher(teacher['teacherID'])):
                    print('删除成功')
                else:
                    print('删除失败')

        elif (cmd == 'q'):
            return

###################教师管理#######################


def printTeacherMenu():
    print('''
<1>     分配课程
<2>     查询课程
<q>     返回上级菜单
    ''')


def allocateCourse(teacherID):
    teacher = getTeacherByID(teacherID)
    deptID = teacher[0]['departmentID']
    course = getDepartmentCourse(deptID)
    if (len(course) == 0):
        print('暂无课程！')
        return
    printHeader(course[0])
    printTable(course)
    courseID = input('请输入要分配的课程：')
    if (courseID == ''):
        print('输入错误！')
        return
    if (getCourseByID(int(courseID)) == None):
        print('无该课程！')
        return


def getTeacherCourse(teacherID):
    course = getCoursebyTeacherID(teacherID)
    if (len(course) == 0):
        print('尚无课程！')
        return
    printHeader(course[0])
    printTable(course)


def teacherQuery(nav, t, data):
    newNav = deepcopy(nav)
    newNav.append(t + '查询')
    printNav(newNav)
    if (t == '姓名'):
        teacher = getTeacherByName(data)
    elif (t == '教工号'):
        teacher = getTeacherByTeacherNumber(data)
    elif (t == 'ID'):
        teacher = getTeacherByID(data)
    if (len(teacher) == 0):
        print('未找到相关教师！')
        return
    printHeader(teacher[0])
    printTable(teacher)


def queryTeacherLoop(nav):
    """
    查询教师
    """
    newNav = deepcopy(nav)
    newNav.append('查询教师')
    while (True):
        printNav(newNav)
        print('''
<1>     教师列表
<2>     按姓名查询
<3>     按教工号查询
<4>     按ID查询
<q>     退出
        ''')
        cmd = input('请输入命令：')
        if (cmd == '1'):
            teacher = getTeacher()
            if (len(teacher) == 0):
                print('暂无教师')
                break
            printHeader(teacher[0])
            printTable(teacher)
        elif (cmd == '2'):
            teacherQuery(newNav, '姓名', input('请输入姓名：'))
        elif (cmd == '3'):
            teacherQuery(newNav, '教工号', input('请输入教工号：'))
        elif (cmd == '4'):
            teacherQuery(newNav, 'ID', input('请输入ID：'))
        elif (cmd == 'q'):
            break
        else:
            print('输入错误！')
            continue


def uniqueTeacherLoop(nav):
    teacher = getTeacher()
    if (len(teacher) == 0):
        print('暂无教师！')
        return
    printHeader(teacher[0])
    printTable(teacher)
    teacherID = input('请输入教师ID:')
    if (teacherID == ''):
        print('输入错误！')
        return
    thisTeacher = getTeacherByID(teacherID)
    if (len(thisTeacher) == 0):
        print('无此教师！')
        return
    newNav = deepcopy(nav)
    newNav.append(thisTeacher[0]['teacherName'])
    while (True):
        printNav(newNav)
        printTeacherMenu()
        cmd = input('请输入命令：')
        if (cmd == '1'):
            allocateCourse(teacherID)
        elif (cmd == '2'):
            getTeacherCourse(teacherID)
        elif (cmd == 'q'):
            break
        else:
            print('输入错误！')
            continue


def teacherMenuLoop(nav):
    newNav = deepcopy(nav)
    newNav.append('教师管理')
    while (True):
        printNav(newNav)
        print('''
<1>     查询教师
<2>     教师管理
<q>     退出
        ''')
        cmd = input('请输入命令：')
        if (cmd == '1'):
            queryTeacherLoop(newNav)
        elif (cmd == '2'):
            uniqueTeacherLoop(newNav)
        elif (cmd == 'q'):
            break
        else:
            print('输入错误！')
            continue
