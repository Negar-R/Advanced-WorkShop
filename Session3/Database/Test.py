import sqlite3

def db_connection(dbName):
    try:
        conn = sqlite3.connect(dbName)
        return conn
    except Exception as e:
        raise e   

conn = db_connection("chatRoom.db") #return a connection object

cursor = conn.cursor()

# cursor.execute("CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255) , age INTEGER CHECK(age > 15), gender BOOLEAN , country VARCHAR(255))")

userss =[('Negar' , 19 , True , 'Iran') , 
        ('Nasim' , 18 , True , 'Canada') , 
        ('Navid' , 22 , False , 'France') ,
        ('Nima' , 21 , False , 'China')]

cursor.executemany("INSERT INTO users(name , age , gender , country)VALUES(?,?,?,?)" , userss)

conn.commit() #after changes you shoul to commit them

cursor.execute("SELECT * From users")

user_db_list = cursor.fetchall() #read the db

for i in user_db_list:
    print(i)

cursor.close()
conn.close()

# dbCone = sqlite3.connect('Chat.db')

# db = dbCone.cursor()
# # db.execute("CREATE TABLE user(id INTEGER PRIMARY KEY , name VARCHAR255 , age integer , gender VARCHAR255 , country VARCHAR255)")


# userss =[('Negar' , 12 , 'Female' , 'Iran') , 
#         ('Nasim' , 18 , 'Female' , 'Canada') , 
#         ('Navid' , 22 , 'Male' , 'France') ,
#         ('Nima' , 21 , 'Male' , 'China')]

# db.executemany("INSERT INTO user(name , age , gender , country)VALUES(?,?,?,?)" , userss)

# # db.execute("INSERT INTO user(name , age , country)VALUES('Nasim' , 13 , 'Female' , 'Canada')")


# # dbCone.commit()
# # db.execute("select * from Userss")
# # a = db.fetchall()
# # print(a)

# db.execute("select * from user where age > 15")
# b = db.fetchall()
# print(b)

# print("__________________")

# db.execute("DELETE FROM user WHERE age < 20 ")
# dbCone.commit()
# dbCone.rollback()
# c = db.fetchall()
# print(c)

