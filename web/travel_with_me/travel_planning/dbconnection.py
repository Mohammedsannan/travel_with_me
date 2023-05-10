import pymysql

def iud(qry,val):
    con=pymysql.connect(host='localhost',port=3308,user='root',password='123456789',db='travel')
    cmd=con.cursor()
    cmd.execute(qry,val)
    id=cmd.lastrowid
    con.commit()
    con.close()
    return id

def selectone(qry,val):
    con=pymysql.connect(host='localhost',port=3308,user='root',password='123456789',db='travel')
    cmd=con.cursor()
    cmd.execute(qry,val)
    res=cmd.fetchone()

    return res

def selectall(qry):
    con=pymysql.connect(host='localhost',port=3308,user='root',password='123456789',db='travel')
    cmd=con.cursor()
    cmd.execute(qry)
    res=cmd.fetchall()
    return res
def selectall2(qry,val):
    con=pymysql.connect(host='localhost',port=3308,user='root',password='123456789',db='travel')
    cmd=con.cursor()
    cmd.execute(qry,val)
    res=cmd.fetchall()
    return res