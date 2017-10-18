import MySQLdb as sql
import os
import add_staff
import delete_staff
import view_staff
import search_staff

def option_menu():
    option =0
    print "1)Add staff\n2)Remove staff\n3)View all\n4)Search"
    option = int(raw_input("Enter your option :"))
    return option

def staff_database_main_menu():
    option =1
    os.system('clear')
    while option<=1 and option<=6:
        db = sql.connect("localhost","arpit","Test@12345","hotel")
        cursor = db.cursor()
        option = option_menu()
        if option == 1:
            add_staff.add(db,cursor)
        elif option ==2:
            delete_staff.delete(db,cursor)
        elif option ==3:
            view_staff.view(db,cursor)
        elif option ==4:
            search_staff.search_staff_main_menu(db,cursor)

