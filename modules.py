from DB import DB

db = DB()

###################查询课程#################
def getCourse():
    """
    获取所有课程
    """
    sql = """select * from course"""
    db.cur.execute(sql)
    return db.cur.fetchall()

def getCoursefromId(cId):
    """
    根据id查询课程
    """
    sql = """select * from course where cId = '{}'""" .format(cId)
    db.cur.execute(sql)
    return db.cur.fetchall()

def getCoursefromName(cName):
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



###########################################
#添加课程
def addNewCourse(cName,cDepart,cTeacher):
    """
    添加课程
    """
    sql = 'insert into course(cName,cDepart,cTeacher) values({},{},{})'.format(cName,cDepart,cTeacher)
    db.cur.execute(sql)



###########删除课程##########
def delCoursefromID(cId):
    """
    根据课程id删除课程
    """
    sql="""DELETE FROM course WHERE  cId = '{}'""" .format(cId)

def delCoursefromName(cName):
    """
    根据课程名称删除课程
    """
    sql="""DELETE FROM course WHERE  cName like '%{}%'""" .format(cName)


###############修改课程############
def modfCourse(cId,cName,cDepart,cTeacher):
    """
    修改对应id的课程信息
    """
    sql="""UPDATE course SET cName='{}',cDepart='{}',cTeacher='{}' WHERE  cId = '{}' """.format(cName,cDepart,cTeacher,cId)

