import MySQLdb as sql
import os
import add_occupant
import delete_occupant
import view_occupant
import search_occupant

def option_menu():
    option =0
    print "1)Add occupant\n2)Remove occupant\n3)View occupant\n4)Search"
    option = int(raw_input("Enter your option :"))
    return option
def occupant_database_main_menu():
    option =1
    os.system('clear')
    while option<=1 and option<=6:
        db = sql.connect("localhost","arpit","Test@12345","hotel")
        cursor = db.cursor()
        option = option_menu()
        if option ==1:
            add_occupant.add(db,cursor)
        elif option ==2:
            delete_occupant.delete(db,cursor)
        elif option ==3:
            view_occupant.view(db,cursor)
        elif option ==4:
            search_occupant.search_occupant_main_menu(db,cursor)

