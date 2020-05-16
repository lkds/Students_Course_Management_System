from DB import DB

db = DB()


def getCourse():
    sql = """select * from student"""
    db.cur.execute(sql)
    return db.cur.fetchone()
