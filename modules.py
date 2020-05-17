
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
    createDict['values'] = ','.join(str(item) for item in data.values())
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
    updateDict['newVal'] = ','.join(k + '=' + str(v) for (k, v) in data)
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
    # sql = """select * from student"""
    # db.cur.execute(sql)
    # return db.cur.fetchall()

    return generalGet('student')


def getStudentByID(studentID):
    """
    根据学生ID获取学生
    """
    # sql = """select * from student where studentID = {}""".format(studentID)
    # db.cur.execute(sql)
    # return db.cur.fetchone()

    return generalGet('student', 1, 'studentID='+studentID)


def getStudentBystudentNumber(studentNumber):
    """
    根据学号获取学生
    """
    # sql = """select * from student where studentNumber = {}""".format(
    #     studentNumber)
    # db.cur.execute(sql)
    # return db.cur.fetchone()
    return generalGet('student', 1, 'studentNumber = '+studentNumber)


def getStudentByName(studentName):
    """
    根据学生姓名获取学生
    """
    # sql = '''
    #     select *
    #     from student
    #     where studentName like '%{}'
    # '''.format(studentName)
    # db.cur.execute(sql)
    # return db.cur.fetchmany()
    return generalGet('student', 0, 'studentNumber like %'+studentName)


def selectCourseByID(studentID, courseID):
    """
    学生选课
    """
    # sql = '''insert into sc(studentID,courseID) values ({},{})'''.format(
    #     studentID, courseID)
    # try:
    #     db.cur.execute(sql)
    #     db.conn.commit()
    #     return True
    # except Exception as e:
    #     db.conn.rollback()
    #     print(e)
    #     return False

    return generalCreate('sc', {'studentID': studentID, 'courseID': courseID})


def quitCourseByID(scID):
    """
    根据scID退课
    """
    # sql = '''
    #     delete from sc where scID = {}
    # '''.format(scID)
    # try:
    #     db.cur.execute(sql)
    #     db.conn.commit()
    # except:
    #     db.conn.rollback()

    return generalDelete('sc', 'scID = '+scID)


def quitCourseBycourseID(courseID):
    '''
    根据课程的id删除学生的选课记录
    '''
    # sql = '''
    #     delete from sc where courseID = '{}'
    # '''.format(courseID)
    # try:
    #     db.cur.execute(sql)
    #     db.conn.commit()
    # except:
    #     db.conn.rollback()
    return generalDelete('sc', 'courseID = '+courseID)


def quitCourseBycourseName(courseName):
    '''
    根据课程的名称删除学神的选课记录
    '''
    # sql = '''
    #     delete from sc in (select sc.* from sc,course where sc.courseID = course.ID and course.courseName = '{}')
    # '''.format(courseName)
    # try:
    #     db.cur.execute(sql)
    #     db.conn.commit()
    # except:
    #     db.conn.rollback()

    return generalDelete('sc', 'scID in (select sc.scID from sc,course where sc.courseID = course.ID and course.courseName = '+courseName+')')


def quitCourseByCourseID(studentID, courseID):
    """
    根据学生ID和课程ID退课
    """
    # sql = '''
    #     delete from sc where studentID = {} and courseID = {}
    # '''.format(studentID, courseID)
    # try:
    #     db.cur.execute(sql)
    #     db.conn.commit()
    #     return True
    # except Exception as e:
    #     db.conn.rollback()
    #     print(e)
    #     return False

    return generalDelete('sc', 'studentID = {} and courseID = {}'.format(studentID, courseID))


def updateGradeByID(scID, grade):
    """
    根据scID更新/添加成绩
    """
    # sql = '''
    #         update sc set grades = {} where scID = {}
    #     '''.format(grade, scID)
    # try:
    #     db.cur.execute(sql)
    #     db.conn.commit()
    # except:
    #     db.conn.rollback()

    return generalUpdate('sc', {'grade': grade}, 'scID = {}'.format(scID))


def getStudentAllCourse(studentID):
    """
    根据ID获取一个学生的所有已选课程
    """
    # sql = """
    #     select course.*
    #     from course,sc
    #     where sc.studentID = {} and sc.courseID = course.courseID
    # """.format(studentID)
    # db.cur.execute(sql)
    # return db.cur.fetchall()

    return generalGet('course,sc', 0, 'sc.studentID = {} and sc.courseID = course.courseID'.format(studentID), ['course.*'])


def getStudentSelectedCourseByCourseID(studentID, courseID):
    # sql = """select * from sc where studentID = {} and courseID = {}""".format(
    #     studentID, courseID)
    # db.cur.execute(sql)
    # return db.cur.fetchone()

    return generalGet('sc', 0, 'studentID = {} and courseID = {}'.format(studentID, courseID))


def getStudentGrade(studentID):
    # sql = """select courseID,grades from sc where studentID = {} and grades != Null""".format(
    #     studentID)
    # db.cur.execute(sql)
    # return db.cur.fetchall()

    return generalGet('sc', 0, 'studentID = {} and grades != Null'.format(studentID), ['courseID', 'grades'])
###################查询课程#################


def getCourse():
    """
    获取所有课程
    """
    # sql = """select * from course"""
    # try:
    #     db.cur.execute(sql)
    #     db.conn.commit()
    # except:
    #     db.conn.rollback()
    # return db.cur.fetchall()

    return generalGet('course')


def getCourseByID(courseID):
    """
    根据id查询课程
    """
    # sql = """select * from course where courseID = '{}'""" .format(courseID)
    # try:
    #     db.cur.execute(sql)
    #     db.conn.commit()
    # except:
    #     db.conn.rollback()
    # return db.cur.fetchall()

    return generalGet('course', 1, 'courseID = \'{}\''.format(courseID))


def getCourseByName(courseName):
    """
    根据课程名字模糊查询课程
    """
    # sql = """select * from course where  courseName like '%{}%'""" .format(
    #     courseName)
    # try:
    #     db.cur.execute(sql)
    #     db.conn.commit()
    # except:
    #     db.conn.rollback()
    # return db.cur.fetchall()

    return generalGet('course', 0, 'courseName like \'%{}%\''.format(courseName))


def getCoursebyTeacherID(teacherID):
    """
    根据教师id查询该老师任课的课程
    """
    # sql = """select * from course where  teacherId = '{}'""" .format(teacherID)
    # try:
    #     db.cur.execute(sql)
    #     db.conn.commit()
    # except:
    #     db.conn.rollback()
    # return db.cur.fetchall()

    return generalGet('course', 0, 'teacherID = {}'.format(teacherID))


def getCoursebyTeacherName(teacherName):
    """
    根据老师的姓名模糊查询该老师任课的课程
    """
    # sql = """select c.* from course c , Teacher t where t.teacherID = c. and teacherName like '%{}%'""" .format(
    #     teacherName)
    # try:
    #     db.cur.execute(sql)
    #     db.conn.commit()
    # except:
    #     db.conn.rollback()
    # return db.cur.fetchall()

    return generalGet('course,teacher', 0, 'teacher.teacherID = course.teacherID and teacherName like \'%{}%\''.format(teacherName), ['course.*'])


def getCoursebycourseCredit(courseCredit):
    """
    根据学分查询课程
    """
    # sql = """select * from course where courseCredit = '{}'""" .format(
    #     courseCredit)
    # try:
    #     db.cur.execute(sql)
    #     db.conn.commit()
    # except:
    #     db.conn.rollback()
    # return db.cur.fetchall()
    return generalGet('course',0,'courseCredit = \'{}\''.format( courseCredit))

# 添加课程


def addNewCourse(courseName, departmentID, teacherID, courseCredit):
    """
    添加课程
    """
    # sql = """insert into course(courseName,departmentID,teacherID,courseCredit) values('{}','{}','{}','{}')""".format(
    #     courseName, departmentID, teacherID, courseCredit)
    # try:
    #     db.cur.execute(sql)
    #     db.conn.commit()
    # except:
    #     db.conn.rollback()
    return generalCreate('course',{'courseName':courseName,'departmentID':courseName,'teacherID':courseName,'courseCredit':courseName})


def delCourseByID(courseID):
    """
    根据课程id删除课程
    """
    # sql = """DELETE FROM course WHERE  courseID = '{}'""".format(courseID)
    # try:
    #     db.cur.execute(sql)
    #     db.conn.commit()
    # except:
    #     db.conn.rollback()
    return generalDelete('course','courseID = {}'.format(courseID))

def delCourseByName(courseName):
    """
    根据课程名称删除课程
    """
    # sql = """DELETE FROM course WHERE  courseName like '%{}%'""".format(
    #     courseName)
    # try:
    #     db.cur.execute(sql)
    #     db.conn.commit()
    # except:
    #     db.conn.rollback()
    return generalDelete('course','courseName like \'%{}%\''.format(courseName))


def updateCourse(courseID, courseName, departmentID, teacherID, courseCredit):
    """
    修改对应id的课程信息
    """
    # sql = """UPDATE course SET courseName='{}',departmentID='{}',teacherID='{}' ,courseCredit = '{}'WHERE  courseID = '{}' """.format(
    #     courseName, departmentID, teacherID, courseCredit, courseID)
    # try:
    #     db.cur.execute(sql)
    #     db.conn.commit()
    # except:
    #     db.conn.rollback()
    # return generalUpdate
    return generalUpdate('course', {'courseName':courseName, 'departmentID':departmentID,' teacherID':teacherID, 'courseCredit':courseCredit}, 'courseID = {}'.format(courseID))


def getTeacher():
    sql = """select * from teacher"""
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()
    return db.cur.fetchall()


def getTeacherByID(teacherID):
    sql = """select * from teacher where teacherID = {} """.format(
        teacherID)
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()
    return db.cur.fetchone()

####### 学院相关 #####


def getDepartmentInfo():
    '''  获取所有学院信息
    '''
    sql = """select * from department"""
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()
    return db.cur.fetchall()


def getDepartmentId(DepartmentId):
    '''
    根据学院id查找学院
    '''
    sql = """select * from department WHERE DepartmentId = '{}'""".format(
        DepartmentId)
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()
    return db.cur.fetchall()


def getDepartmentInfoByName(departmentName):
    ''' 根据学院名获取学院信息 '''
    sql = """select * from department
    where departmentName = '{}' """.format(departmentName)
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()
    return db.cur.fetchone()


def modifyDepartmentInfo(departmentInfo):
    '''修改学院信息，参数为dict'''
    sql = """update department set departmentName = '{}',
    departmentAddress ='{}', contactInformation = '{}'
    where departmentID = {}
    """.format(departmentInfo['departmentName'], departmentInfo['departmentAddress'], departmentInfo['contactInformation'],
               departmentInfo['departmentID'])
    try:
        db.cur.execute(sql)
        db.conn.commit()
        print("修改成功")
    except:
        db.conn.rollback()
        print("修改失败")


def getDepartmentStudent(departmentName):
    '''  获取学院所有学生 '''

    sql = """select * from student 
    where departmentID = 
    (select departmentID from department where departmentName = '{}')""".format(departmentName)
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()
    return db.cur.fetchall()


def getDepartmentCourse(departmentName):
    '''  获取学院所有课程 '''

    sql = """select * from course
    where departmentID = 
    (select departmentID from department where departmentName = '{}')""".format(departmentName)
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()
    return db.cur.fetchall()


def getDepartmentTeacher(departmentName):
    '''  获取学院所有老师 '''
    sql = """select * from teacher where departmentID = (select departmentID from department where departmentName = '{}')""".format(
        departmentName)
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()
    return db.cur.fetchall()


def addStudent(studentInfo):
    sql = """insert into student(departmentID,name,studentNumber,gender,grade,birthday)
    values({},{},'{}','{}','{}','{}')
    """.format(studentInfo['departmentID'], studentInfo['name'], studentInfo['studentNumber'], studentInfo['gender'],
               studentInfo['grade'], studentInfo['birthday'])
    try:
        db.cur.execute(sql)
        db.conn.commit()
        print("添加成功")
    except:
        db.conn.rollback()
        print("添加失败")


def deleteStudent(studentNumber):
    '''删除指定number的学生'''
    sql = """Delete  from student where studentNumber = '{}'""".format(
        studentNumber)
    try:
        db.cur.execute(sql)
        db.conn.commit()
        print("删除成功")
    except:
        db.conn.rollback()
        print("删除失败")


def addTeacher(teacherInfo):
    '''添加老师,参数为字典'''
    sql = """insert into teacher(departmentID,teacherNumber,birthday,title,gender,office,homeAddress)
    values('{}','{}','{}','{}','{}','{}','{}')
    """.format(teacherInfo['departmentID'], teacherInfo['teacherNumber'], teacherInfo['birthday'], teacherInfo['title'],
               teacherInfo['gender'], teacherInfo['office'], teacherInfo['homeAddress'])
    try:
        db.cur.execute(sql)
        db.conn.commit()
        print("添加成功")
    except:
        db.conn.rollback()
        print("添加失败")


def deleteTeacher(teacherID):
    '''删除指定ID的老师'''
    sql = """Delete  from teacher where teacherID = {}""".format(teacherID)
    try:
        db.cur.execute(sql)
        db.conn.commit()
        print("删除成功")
    except:
        db.conn.rollback()
        print("删除失败")
