import os
import time

def add(db,cursor):
    sid = int(raw_input("Staff ID :"))
    name = str(raw_input("Name :"))
    dept = str(raw_input("Dept :"))
    sal = int(raw_input("Salary :"))
    com = """INSERT INTO STAFF VALUES('%d','%s','%s','%d')"""%(sid,name,dept,sal)
    try:
        cursor.execute(com)
        db.commit()
        print "Added Staff successfully"
        db.close()
    
    except:
        db.rollback()
        db.close()
        print "Error while adding staff"
    time.sleep(0.7)
    os.system('clear')


