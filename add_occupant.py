import os
import time

def add(db,cursor):
    oid = int(raw_input("Occupant ID = "))
    name = str(raw_input("Occupant name = "))
    rno = int(raw_input("Room number = "))
    duration = int(raw_input("Duration ="))
    com1 = """INSERT INTO OCCUPANT VALUES('%d','%s','%d','%d')"""%(oid,name,rno,duration)
    com2 = """UPDATE ROOM SET STATUS='OCCUPIED' WHERE RNO='%d'"""%(rno)
    try:
        cursor.execute(com1)
        cursor.execute(com2)
        db.commit()
        print "Added occupant successfully"
        db.close()
    except:
        db.rollback()
        db.close()
        print "Error while adding occupant"
    time.sleep(0.7)
    os.system('clear')

