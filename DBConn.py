import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","dbuser","dbuser","testDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

#inserting data
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
        VALUES('MD ASADUL','ISLAM',28,'M',1908)"""

try:
    cursor.execute(sql)
    db.commit();
except:
    db.rollback();
db.close()