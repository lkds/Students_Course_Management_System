from DB import DB

db = DB()

#########################学生模块#######################


def getStudent():
    """
    获取所有的学生
    """
    sql = """select * from student"""
    db.cur.execute(sql)
    return db.cur.fetchmany()


def getStudentByID(studentID):
    """
    根据学生ID获取学生
    """
    sql = """select * from student where studentID = {}""".format(studentID)
    db.cur.execute(sql)
    return db.cur.fetchone()


def getStudentByName(studentName):
    """
    根据学生姓名获取学生
    """
    sql = '''
        select * 
        from student
        where studentName like '%{}'
    '''.format(studentName)
    db.cur.execute(sql)
    return db.cur.fetchmany()


def selectCourseByID(studentID, courseID):
    """
    学生选课
    """
    sql = '''
        insert into sc values ({},{})
    '''.format(studentID, courseID)
    db.cur.execute(sql)


def quitCourseByID(scID):
    """
    根据scID退课
    """
    sql = '''
        delete from sc where scID = {}
    '''.format(scID)
    db.cur.execute(sql)


def updateGradeByID(scID, grade):
    """
    根据scID更新/添加成绩
    """
    sql = '''
            update sc set grades = {} where scID = {}
        '''.format(grade, scID)
    db.cur.execute(sql)


def getStudentAllCourse(studentID):
    """
    根据ID获取一个学生的所有已选课程
    """
    sql = """
        select course.*
        from course,sc
        where sc.studentID = {} and sc.courseID = course.courseID
    """.format(studentID)
    db.cur.execute(sql)
    return db.cur.fetchall()

###################查询课程#################


def getCourse():
    """
    获取所有课程
    """
    sql = """select * from course"""
    db.cur.execute(sql)
    return db.cur.fetchall()


def getCourseByID(cId):
    """
    根据id查询课程
    """
    sql = """select * from course where cId = '{}'""" .format(cId)
    db.cur.execute(sql)
    return db.cur.fetchall()


def getCourseByName(cName):
    """
    根据课程名字模糊查询课程
    """
    sql = """select * from course where  cName like '%{}%'""" .format(cName)
    db.cur.execute(sql)
    return db.cur.fetchall()

def getCoursebyTeacherID(teacherId):
    """
    根据教师id查询该老师任课的课程
    """
    sql = """select * from course where  teacherId = '{}'""" .format(teacherId)
    db.cur.execute(sql)
    return db.cur.fetchall()

def getCoursebyTeacherName(teacherName):
    """
    根据老师的姓名模糊查询该老师任课的课程
    """
    sql = """select c.* from course c , Teacher t where t.teacherID = c. and teacherName like '%{}%'""" .format(teacherName)
    db.cur.execute(sql)
    return db.cur.fetchall()



# 添加课程
def addNewCourse(cName, cDepart, cTeacher):
    """
    添加课程
    """
    sql = '''insert into course(courseName,departmentID,teacherID) values('{}',{},{})'''.format(
        cName, cDepart, cTeacher)
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()


def delCourseByID(cId):
    """
    根据课程id删除课程
    """
    sql = """DELETE FROM course WHERE  cId = '{}'""".format(cId)
    db.cur.execute(sql)


def delCourseByName(cName):
    """
    根据课程名称删除课程
    """
    sql = """DELETE FROM course WHERE  cName like '%{}%'""".format(cName)
    db.cur.execute(sql)


def updateCourse(cId, cName, cDepart, cTeacher):
    """
    修改对应id的课程信息
    """
    sql = """UPDATE course SET courseName='{}',department='{}',cTeacher='{}' WHERE  cId = '{}' """.format(
        cName, cDepart, cTeacher, cId)
    db.cur.execute(sql)
