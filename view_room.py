import os
import time
from prettytable import PrettyTable as pt

def view(db,cursor):
    os.system('clear')
    com = """SELECT * FROM ROOM"""
    row_list = []
    table_list = []
    cursor.execute(com)
    results = cursor.fetchall()
    for row in results:
        row_list.append(row[0])
        row_list.append(row[1])
        row_list.append(row[2])
        row_list.append(row[3])
        table_list.append(row_list)
        row_list = []
    t=pt(['RoomNo','Status','Type','Cost'])
    for row in table_list:
        t.add_row(row)
    os.system('clear')
    print t
    raw_input("Press any key to continue...")
