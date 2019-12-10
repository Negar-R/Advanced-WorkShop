from datetime import datetime
import pickle
import uuid

listOfMemberInfo = []

class Members():
    def __init__(self , name , age):
        self.name = name 
        self.age = age
        self.iD = None
        self.rentedBook = []
        self.date = datetime.now()

    def idGenerator(self):
        self.iD = uuid.uuid1()
        # print(self.iD)

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
        member_info = {'Name' : self.name , 'Age' : self.age , 'Id' : self.iD , 'Register Date' : self.date
         , 'List of borrowed books' : self.rentedBook}
        listOfMemberInfo.append(member_info)
        with open('Members' , 'wb') as m:
            pickle.dump(listOfMemberInfo , m)

    def getListOfBorrowedBook(self):
        for i in range(len(listOfMemberInfo)):
            if listOfMemberInfo[i]['Name'] == self.name and listOfMemberInfo[i]['Id'] == self.iD:
                print(listOfMemberInfo[i]['List of borrowed books'])

        # with open('Members' , 'rb') as m:
        #     data = pickle.load(m)
        # print(data)    





# mm = Members('Negar' , 20)
# mm.addMember()

# print("name : " , m.name)
# n = Members('Nasim' , 18)
# n.idGenerator()
# m.expireCheck()
# n.expireCheck()

