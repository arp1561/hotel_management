import MySQLdb as sql

db = sql.connect("localhost","arpit","Test@12345","library")
cursor = db.cursor()

id = int(raw_input("ID :"))
name = str(raw_input("Name :"))
dept = str(raw_input("Dept :"))
salary = int(raw_input("Salary :"))

com = """INSERT INTO STAFF VALUES('%d','%s','%s','%d')"""%(id,name,dept,salary)


