
from DB import DB

db = DB()

#########################通用CURD######################


def generalGet(tbName, row=0, condition='', keys='*'):
    """
    通用数据获取函数
    :param tbName:[str] 需要获取的数据表名
    :param keys:[list] 需要获取的字段,空表示所有
    :param condition:[str] 选择条件,''表示无条件
    :param row:[int] 需要的条数，0表示所有 
    :return [list] 数据列表
    """
    queryDict = dict()
    queryDict['tbName'] = tbName
    queryDict['keys'] = '*' if len(keys) == 0 else ','.join(keys)
    queryDict['condition'] = 'true' if condition == '' else condition
    sql = """
select {keys}
from {tbName}
where {condition}
    """.format(**queryDict)
    db.cur.execute(sql)
    if (row == 0):
        return db.cur.fetchall()
    else:
        return db.cur.fetchmany(row)


def generalCreate(tbName, data):
    """
    通用插入数据函数
    :param tbName:[str] 表明
    :param data:[dict] 字段值
    :return [bool] 操作结果
    """
    createDict = dict()
    createDict['tbName'] = tbName
    createDict['field'] = ','.join(data.keys())
    createDict['values'] = ','.join(
        '\'' + str(item) + '\'' if type(item) != int else str(item) for item in data.values())
    sql = '''
insert into {tbName}({field})
values ({values})
    '''.format(**createDict)
    try:
        db.cur.execute(sql)
        db.conn.commit()
        return True
    except Exception as e:
        db.conn.rollback()
        print(e)
        return False


def generalUpdate(tbName, data, condition):
    """
    通用更新函数
    :param tbName:[str] 表名
    :param data:[dict] 字段和值（部分或全部）
    :param condition:[str] 条件
    :return [bool] 操作结果
    """
    updateDict = dict()
    updateDict['tbName'] = tbName
    updateDict['newVal'] = ','.join(k + '=' + '\'' + str(v) + '\''
                                    if type(v) != int else k + '=' + str(v) for k, v in data.items())
    updateDict['condition'] = condition
    sql = '''
update {tbName}
set {newVal}
where {condition}
    '''.format(**updateDict)
    try:
        db.cur.execute(sql)
        db.conn.commit()
        return True
    except Exception as e:
        db.conn.rollback()
        print(e)
        return False


def generalDelete(tbName, condition):
    """
    通用删除模块
    :param tbName:[str] 表名
    :param condition:[str] 限制条件
    :return [bool] 操作结果
    """
    deleteDict = dict()
    deleteDict['tbName'] = tbName
    deleteDict['condition'] = condition
    sql = """
delete from {tbName}
where {condition}
    """.format(**deleteDict)
    try:
        db.cur.execute(sql)
        db.conn.commit()
        return True
    except Exception as e:
        db.conn.rollback()
        print(e)
        return False
#########################学生模块#######################


def getStudent():
    """
    获取所有的学生
    """
    return generalGet('student,department', 0, 'student.departmentID = department.departmentID', ['student.*', 'department.departmentName'])


def getStudentByID(studentID):
    """
    根据学生ID获取学生
    """
    condition = 'studentID={}'.format(studentID)
    return generalGet('student', 0, condition)


def getStudentBystudentNumber(studentNumber):
    """
    根据学号获取学生
    """
    return generalGet('student', 0, 'studentNumber = '+studentNumber)


def getStudentByName(studentName):
    """
    根据学生姓名获取学生
    """
    return generalGet('student', 0, 'name like \'%{}%\''.format(studentName))


def selectCourseByID(studentID, courseID):
    """
    学生选课
    """

    return generalCreate('sc', {'studentID': studentID, 'courseID': courseID})


def quitCourseByID(scID):
    """
    根据scID退课
    """

    return generalDelete('sc', 'scID = '+scID)


def quitCourseBycourseID(courseID):
    '''
    根据课程的id删除学生的选课记录
    '''
    return generalDelete('sc', 'courseID = '+courseID)


def quitCourseBycourseName(courseName):
    '''
    根据课程的名称删除学生的选课记录
    '''

    return generalDelete('sc', 'scID in (select sc.scID from sc,course where sc.courseID = course.courseID and course.courseName = '+courseName+')')


def quitCourseByCourseID(studentID, courseID):
    """
    根据学生ID和课程ID退课
    """

    return generalDelete('sc', 'studentID = {} and courseID = {}'.format(studentID, courseID))


def updateGradeByID(scID, grade):
    """
    根据scID更新/添加成绩
    """

    return generalUpdate('sc', {'grades': grade}, 'scID = {}'.format(scID))


def updateGradeByStudentIDAndCourseID(studentID, courseID, grade):
    """
    根据studentID,courseID更新/添加成绩
    """
    return generalUpdate('sc', {'grades': grade}, 'studentID = {} AND courseID = {}'.format(studentID, courseID))


def getStudentAllCourse(studentID):
    """
    根据ID获取一个学生的所有已选课程
    """

    return generalGet('course,sc', 0, 'sc.studentID = {} and sc.courseID = course.courseID'.format(studentID), ['course.*'])


def getStudentSelectedCourseByCourseID(studentID, courseID):

    return generalGet('sc', 0, 'studentID = {} and courseID = {}'.format(studentID, courseID))


def getStudentGrade(studentID):
    """
    获取成绩并计算GPA
    """
    return generalGet('sc,course', 0, 'studentID = {} and course.courseID = sc.courseID and grades is not Null'.format(studentID), ['sc.courseID as courseID', 'grades', 'courseName', 'courseCredit'])
###################查询课程#################


def getCourse():
    """
    获取所有课程
    """

    return generalGet('course,department,teacher', 0,
                      'course.teacherID = teacher.teacherID AND course.departmentID = department.departmentID',
                      ['course.*', 'teacher.teacherName', 'department.departmentName'])


def getCourseByID(courseID):
    """
    根据id查询课程
    """

    return generalGet('course', 1, 'courseID = \'{}\''.format(courseID))


def getCourseByName(courseName):
    """
    根据课程名字模糊查询课程
    """

    return generalGet('course', 0, 'courseName like \'%{}%\''.format(courseName))


def getCoursebyTeacherID(teacherID):
    """
    根据教师id查询该老师任课的课程
    """

    return generalGet('course', 0, 'teacherID = {}'.format(teacherID))


def getCoursebyTeacherName(teacherName):
    """
    根据老师的姓名模糊查询该老师任课的课程
    """

    return generalGet('course,teacher', 0, 'teacher.teacherID = course.teacherID and teacherName like \'%{}%\''.format(teacherName), ['course.*'])


def getCoursebycourseCredit(courseCredit):
    """
    根据学分查询课程
    """
    return generalGet('course', 0, 'courseCredit = \'{}\''.format(courseCredit))

# 添加课程


def addNewCourse(courseName, departmentID, teacherID, courseCredit):
    """
    添加课程
    """
    return generalCreate('course', {'courseName': courseName, 'departmentID': departmentID,  'teacherID': teacherID, 'courseCredit': courseCredit})


def delCourseByID(courseID):
    """
    根据课程id删除课程
    """
    return generalDelete('course', 'courseID = {}'.format(courseID))


def delCourseByName(courseName):
    """
    根据课程名称删除课程
    """
    return generalDelete('course', 'courseName like \'%{}%\''.format(courseName))


def updateCourse(newCourse):
    """
    修改对应id的课程信息
    """
    return generalUpdate('course', newCourse, 'courseID = {}'.format(newCourse['courseID']))


def getTeacher():

    return generalGet('teacher,department', 0,
                      'teacher.departmentID = department.departmentID',
                      ['teacher.*', 'department.departmentName'])


def getTeacherByID(teacherID):

    condition = 'teacherID={}'.format(teacherID)
    return generalGet('teacher', 0, condition)


####### 学院相关 #####


def getDepartmentInfo():
    ''' 
    获取所有学院信息
    '''
    return generalGet('department', 0, keys=['departmentID', 'departmentName'])


def getDepartmentById(departmentId):
    '''
    根据学院id查找学院
    '''
    condition = 'departmentID={}'.format(departmentId)
    return generalGet('department', 0, condition)


def getDepartmentByName(departmentName):
    ''' 根据学院名获取学院信息 '''

    condition = """departmentName like '%{}%'""".format(departmentName)
    return generalGet('department', 0, condition)


def modifyDepartmentInfo(departmentInfo):
    '''修改学院信息，参数为dict'''

    condition = 'departmentID={}'.format(departmentInfo['departmentID'])
    return generalUpdate('department', departmentInfo, condition)


def getDepartmentStudent(departmentID):
    '''  获取学院所有学生 '''

    condition = """departmentID = '{}' """.format(
        departmentID)
    return generalGet('student', 0, condition)


def getDepartmentCourse(departmentID):
    '''  获取学院所有课程 '''

    condition = """departmentID = '{}' """.format(
        departmentID)
    return generalGet('course', 0, condition)


def getDepartmentCourseNotAllocated(departmentID):
    '''  获取学院所有未分配课程 '''

    condition = """departmentID = '{}' AND teacherID is null or trim(teacherID)=''""".format(
        departmentID)
    return generalGet('course', 0, condition)


def getDepartmentTeacher(departmentID):
    '''  获取学院所有老师 '''
    condition = """departmentID = '{}' """.format(
        departmentID)
    return generalGet('teacher', 0, condition)


def addStudent(studentInfo):

    return generalCreate('student', studentInfo)


def deleteStudent(studentID):
    '''删除指定number的学生'''

    condition = 'studentID={}'.format(studentID)
    return generalDelete('student', condition)


def addTeacher(teacherInfo):
    # '''添加老师,参数为字典'''
    return generalCreate('teacher', teacherInfo)


def deleteTeacher(teacherID):
    # '''删除指定ID的老师'''
    condition = 'teacherID={}'.format(teacherID)
    return generalDelete('teacher', condition)


#########################教师########################
def getTeacherByName(name):
    return generalGet('teacher', 0, 'teacherName like \'%{}%\''.format(name))


def getTeacherByTeacherNumber(No):
    return generalGet('teacher', 0, 'teacherNumber = {}'.format(No))
