import os
import time

def delete(db,cursor):
    sid = int(raw_input("Staff ID for delete :"))
    com = """DELETE FROM STAFF WHERE SID='%d'"""%(sid)
    try:
        cursor.execute(com)
        db.commit()
        print "Deleted successfully"
        db.close()
    except:
        db.rollback()
        db.close()
    time.sleep(0.7)
    os.system('clear')
