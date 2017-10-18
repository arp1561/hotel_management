import os
import MySQLdb as sql
import view_room
import search_room

def option_menu():
    print "1) View all rooms\n2)Search"
    option = int(raw_input("Enter your option"));
    return option

def room_database_main_menu():
    option =1
    os.system('clear')
    while option <=1 and option<=6:
        db = sql.connect("localhost","arpit","Test@12345","hotel")
        cursor = db.cursor()
        os.system('clear')
        option = option_menu()
        if option ==1:
            view_room.view(db,cursor)
        elif option ==2:
            search_room.search_room_main_menu(db,cursor)

        
        
