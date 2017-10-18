import os
import time
import staff_database
import room_database
import occupant_database

def option_list():
    option = 0
    print "1)Staff Database\n2)Room Database\n3)Occupant Database\n4)Exit"
    option = int(raw_input("Enter your option :"))
    return option

def main():
    option =1
    while option>=1 and option<=3:
        option = option_list()
        if option ==1:
            staff_database.staff_database_main_menu()
        elif option ==2:
            room_database.room_database_main_menu()
        elif option ==3:
            occupant_database.occupant_database_main_menu()
        
if __name__=='__main__':
    main()
