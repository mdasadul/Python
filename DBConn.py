import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","dbuser","dbuser","testDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#create table
sql = """CREATE TABLE EMPLOYEE (
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT)"""
cursor.execute(sql)
db.close()