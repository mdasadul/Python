import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","dbuser","dbuser","testDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

#fetching data from database
fetch_data = """ SELECT * FROM EMPLOYEE""";

try:
    cursor.execute(fetch_data)
    results = cursor.fetchall();
    for row in results:
        fname = row[0];
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print "First Name = %s, Last Name = %s, age =%d, sex = %s, income = %d " % \
        (fname,lname,age,sex,income)
    
    db.commit();
except:
    db.rollback();
db.close()