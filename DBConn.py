import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","dbuser","dbuser","testDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

#fetching data from database
update_data = """ update employee set age = 32 where sex = 'm'""";

try:
    cursor.execute(update_data)
    db.commit();
except:
    db.rollback();
db.close()