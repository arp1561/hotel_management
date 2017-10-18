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
    t = pt(['OID','Name','Rno','Duration'])
    for row in table_list:
        t.add_row(row)
    os.system('clear')
    print t
    raw_input("Press any key to continue...")


def search_occupant_main_menu(db,cursor):
    os.system('clear')
    print "Search by:\n1)OID\n2)Name\n3)Duration"
    option = int(raw_input("Enter your option :"))
    if option ==1:
        value = int(raw_input("Enter the OID :"))
        com = """SELECT * FROM OCCUPANT WHERE OID='%d'"""%(value)
        search(db,cursor,com)
    elif option ==2:
        value = str(raw_input("Enter the Name :"))
        com = """SELECT * FROM OCCUPANT WHERE NAME='%s'"""%(value)
        search(db,cursor,com)
    elif option ==3:
        value = int(raw_input("Enter the Duration :"))
        com = """SELECT * FROM OCCUPANT WHERE DURATION='%d'"""%(value)
        search(db,cursor,com)




