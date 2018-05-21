import sqlite3

path = "C:/EXCELbig/excelbig.db"
conn = sqlite3.connect(path)
c = conn.cursor()


def createTB():
    c.execute("create table LogIN (numbr INTEGER, refCode TEXT, refTitle TEXT, issFrom TEXT, issDataDel REAL, issDate TEXT, respReq BLOB, respRef TEXT, respDataDel REAL, respDate TEXT)")
    
def createTB2():
    c.execute("create table LogOUT (numbr INTEGER, refCode TEXT, refTitle TEXT, issFrom TEXT, issDataDel REAL, issDate TEXT, respReq BLOB, respRef TEXT, respDataDel REAL, respDate TEXT)")

def storeDB(numbr, refCode, refTitle, issFrom, issDataDel, issDate, respReq, respRef, respDataDel, respDate):
    sql = "insert into LogIN(numbr, refCode, refTitle, issFrom, issDataDel, issDate, respReq, respRef, respDataDel, respDate) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    c.execute(sql, (numbr, refCode, refTitle, issFrom, issDataDel, issDate, respReq, respRef, respDataDel, respDate))
    conn.commit()
    
def storeDB2(numbr, refCode, refTitle, issFrom, issDataDel, issDate, respReq, respRef, respDataDel, respDate):
    sql = "insert into LogOUT(numbr, refCode, refTitle, issFrom, issDataDel, issDate, respReq, respRef, respDataDel, respDate) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    c.execute(sql, (numbr, refCode, refTitle, issFrom, issDataDel, issDate, respReq, respRef, respDataDel, respDate))
    conn.commit()
    
def readDB(colname= "*"):
    sql = "select " + colname + " from LogIN"
    c.execute(sql)
    rows = c.fetchall()
    return rows

def readDB2(colname= "*"):
    sql = "select " + colname + " from LogOUT"
    c.execute(sql)
    rows = c.fetchall()
    return rows
