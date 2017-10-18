import os
import time

def delete(db,cursor):
    oid = int(raw_input("Occupant ID for deletion :"))
    rno = int(raw_input("Room no. to vacate :"))
    com1 = """DELETE FROM OCCUPANT WHERE OID='%d'"""%(oid)
    com2 = """UPDATE ROOM SET STATUS = 'VACANT' WHERE RNO='%d'"""%(rno)
    try:
        cursor.execute(com1)
        cursor.execute(com2)
        db.commit()
        print "deleted successfully"
    except:
        db.rollback()
        db.close()
    time.sleep(0.7)
    os.system('clear')

