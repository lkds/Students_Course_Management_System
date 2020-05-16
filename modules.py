
from DB import DB

db = DB()


def getCourse():
    sql = """select * from student"""
    db.cur.execute(sql)
    return db.cur.fetchone()


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
   where departmentName = {}""".format(departmentName)
    try:
        db.cur.execute(sql)
        db.conn.commit()
    except:
        db.conn.rollback()
   return db.cur.fetchall(departmentName)

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
