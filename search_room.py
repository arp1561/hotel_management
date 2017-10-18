import os
import time
from prettytable import PrettyTable as pt

def search(db,cursor,com):
    table_list = []
    row_list = []
    cursor.execute(com)
    results = cursor.fetchall()
    for row in results:
        row_list.append(row[0])
        row_list.append(row[1])
        row_list.append(row[2])
        row_list.append(row[3])
        table_list.append(row_list)
        row_list = []
    t = pt(['Room No','Status','Type','Cost'])
    for row in table_list:
        t.add_row(row)
    os.system('clear')
    print t
    raw_input("Press any key to continue...")
    os.system('clear')


def search_room_main_menu(db,cursor):
    os.system('clear')
    print "Search by\n1)Room no\n2)Occupied rooms\n3)Unoccupied rooms"
    option = int(raw_input("Enter your option :"))
    if option ==1:
        value = int(raw_input("Enter your room no :"))
        com = """SELECT * FROM ROOM WHERE RNO='%d'"""%(value)
        search(db,cursor,com)
    elif option ==2:
        com = """SELECT * FROM ROOM WHERE STATUS='OCCUPIED'"""
        search(db,cursor,com)
    elif option ==3:
        com = """SELECT * FROM ROOM WHERE STATUS='VACANT'"""
        search(db,cursor,com)
    
