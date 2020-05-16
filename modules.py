
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
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()
   return db.cur.fetchall(departmentName)


def quitCourseByID(scID):
    """
    根据scID退课
    """
    sql = '''
        delete from sc where scID = {}
    '''.format(scID)
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()
   return db.cur.fetchall()



def updateGradeByID(scID, grade):
    """
    根据scID更新/添加成绩
    """
    sql = '''
            update sc set grades = {} where scID = {}
        '''.format(grade, scID)
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()



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
    sql = """select * from course where courseID = '{}'""" .format(cId)
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
    sql = """select c.* from course c , Teacher t where t.teacherID = c. and teacherName like '%{}%'""" .format(
        teacherName)
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
   return db.cur.fetchall()


def delCourseByID(cId):
    """
    根据课程id删除课程
    """
    sql = """DELETE FROM course WHERE  cId = '{}'""".format(cId)
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()
 



def delCourseByName(cName):
    """
    根据课程名称删除课程
    """
    sql = """DELETE FROM course WHERE  cName like '%{}%'""".format(cName)
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()



def updateCourse(cId, cName, cDepart, cTeacher):
    """
    修改对应id的课程信息
    """
    sql = """UPDATE course SET courseName='{}',department='{}',cTeacher='{}' WHERE  cId = '{}' """.format(
        cName, cDepart, cTeacher, cId)
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()


####### 学院相关 #####
def getDepartmentCourse():
    ''' 根据学院名获取其开课信息 '''
   sql = """select * from course 
   where departmentID = (select departmentID from department where departmentName = {})""".format(departmentName)
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()
    return db.cur.fetchall()
def getDepartmentInfo():
    '''  获取所有学院信息
    '''

   sql = """select * from Department"""
   try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()
    return db.cur.fetchall()

def getDepartmentInfo(departmentName):
   ''' 根据学院名获取学院信息 '''
   sql = """select * from Department 
   where departmentName = {} """.format(departmentName)
   try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()
    return db.cur.fetchall()
def modifyDepartmentInfo(departmentInfo):
    '''修改学院信息，参数为dict'''
    sql = """update department set departmentName = {},
    departmnetAddress ={}, contactInformation = {}
    where departmentID = {}
    """.format(departmentInfo.departmentName,departmentInfo.departmentAddress,departmentInfo.contactInformation
    departmentInfo.departmentID)
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()

def getDepartmentStudent(departmentName):
       '''  获取学院所有学生 '''

   sql = """select * from student 
   where departmentID = 
   (select departmentID from department where departmentName = {})""".format(departmentName)
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()
   return db.cur.fetchall()
def getDepartmentTeacher(departmentName):
    '''  获取学院所有老师 '''
   sql = """select * from teacher where departmentID = (select departmentID from department where departmentName = {})""".format(departmentName)
   try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()
   return db.cur.fetchall()
def addStudent(studentInfo):
       sql = """insert into student(departmentID,name,studentNumber,gender,grade,birthday)
    values({},{},{},{},{},{},{}
    """.format(studentInfo['departmentID'],studentInfo['name'],studentInfo['studentNumber'],studentInfo['gender'],
    studentInfo['grade'],studentInfo['birthday'])
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()
def deleteStudent(studentNumber):
    '''删除指定number的学生'''
    sql = """Delete  from student where studentNumber = {}""".format(studentNumber)
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()


def addTeacher(teacherInfo):
    '''添加老师,参数为字典'''
    sql = """insert into teacher(departmentID,teacherNumber,birthday,title,gender,office,homeAddress)
    values({},{},{},{},{},{},{}
    """.format(teacherInfo['departmentID'],teacherInfo['teacherNumber'],teacherInfo['birthday'],teacherInfo['title'],
    teacherInfo['gender'],teacherInfo['office'],teacherInfo['homeAddress'])
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()  

def delteteTeacher(teacherID):
    '''删除指定ID的老师'''
    sql = """Delete  from teacher where teacherID = {}""".format(teacherID)
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()
