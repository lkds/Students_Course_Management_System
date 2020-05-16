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
