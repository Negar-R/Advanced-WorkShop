from datetime import datetime
import uuid
import sqlite3

conn = sqlite3.connect("Library.db")
cursorM = conn.cursor()

cursorM.execute("DROP TABLE members")

cursorM.execute("CREATE TABLE IF NOT EXISTS members(ID VARCHAR(255) PRIMARY KEY , NAME VARCHAR(255) , AGE INTEGER , ENTER TEXT , BORROWEDBOOK TEXT)")

cursorM.execute("CREATE TABLE IF NOT EXISTS admins(ID VARCHAR(255) PRIMARY KEY , NAME VARCHAR(255) , AGE INTEGER)")

conn.commit()

class Members():
    def __init__(self , name , age):
        self.name = name 
        self.age = age
        self.iD = None
        self.rentedBook = []
        self.date = datetime.now()

    def idGenerator(self):
        self.iD = str(uuid.uuid1())


    def expireCheck(self):
        t = self.date
        n = datetime.now()

        if (int(t.strftime("%Y")) + 1 == int(n.strftime("%Y")) and 
        t.strftime("%m") == n.strftime("%m")  and
        t.strftime("%d")  == n.strftime("%d")):
            # print("Expired!!")
            return True
        else:
            # print("Have right membership") 
            return False  

    def addMember(self):
        self.idGenerator()
        info = (self.iD , self.name , self.age , self.date)
        cursorM.execute("INSERT INTO members(ID , NAME , AGE , ENTER) VALUES(? , ? , ? , ?)" , info)   
        conn.commit()

    def addAdmin(self):
        self.idGenerator()
        info = (self.iD , self.name , self.age)
        cursorM.execute("INSERT INTO admins(ID , NAME , AGE) VALUES(? , ? , ?)" , info)   
        conn.commit() 

# TEST:

m = Members('Nasim' , 18)
m.addMember()

mm = Members('Negar' , 20)
mm.addMember()

cursorM.execute("SELECT * FROM members")
s = cursorM.fetchall()

for i in s:
    print(i)

# print("------------------")

# a = Members('Hamid' , 30)
# a.addAdmin()

# cursorM.execute("SELECT * FROM admins")
# s = cursorM.fetchall()

# for i in s:
#     print(i)

# conn.close()
