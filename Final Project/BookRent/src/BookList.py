import pickle
import Member

listOfBookInfo = [] 

class Book():
    def __init__(self , name , author , category , international ,  bookId):
        self.name = name
        self.author = author
        self.category = category
        self.bookId = bookId
        self.status = True
        self.rent = None
        self.international = international
        self.motarjem = None 


    def setMotarjem(self , motarjem):
        if self.international:
            self.motarjem = motarjem

    def addBook(self):
        book_info = {'Name' : self.name , 'Author' : self.author , 'Category' : self.category , 
        'International' : self.international , 'Id' : self.bookId , 'Status' : self.status ,
        'Rent' : self.rent}
        listOfBookInfo.append(book_info)
        with open('Books' , 'wb') as b:
            pickle.dump(listOfBookInfo , b)  

    def removeBook(self):
        excit = False 
        ind = 0    
        for i in range(len(listOfBookInfo)): 
            if self.name == listOfBookInfo[i]['Name'] and self.bookId == listOfBookInfo[i]['Id']:
                excit = True
                ind = i
                break
        if excit:
            listOfBookInfo.remove(listOfBookInfo[ind])
            with open('Books' , 'wb') as b:
                pickle.dump(listOfBookInfo , b)

            # print(listOfBookInfo)

    def getInformetionAboutBook(self):
        for i in range(len(listOfBookInfo)):
            if listOfBookInfo[i]['Id'] == self.bookId:
                print(listOfBookInfo[i])


    def rentBook(self , member):
        #type(memeber) = object
        if not self.status:
            print("This Book was rented before")
        if self.status and not member.expireCheck():
            self.rent = member.iD
            self.status = False
            for i in range(len(listOfBookInfo)):
                if listOfBookInfo[i]['Id'] == self.bookId:
                    listOfBookInfo[i]['Status'] = self.status
                    listOfBookInfo[i]['Rent'] = self.rent
            member.rentedBook.append((self.name , self.bookId))   
            # print(member.rentedBook)              
    
    def whoHaveBook(self):
        for i in range(len(Member.listOfMemberInfo)):
            if Member.listOfMemberInfo[i]['Id'] == self.rent:
                print(Member.listOfMemberInfo[i]['Name'] , Member.listOfMemberInfo[i]['Age'] , 
                Member.listOfMemberInfo[i]['Id'])

b = Book('OnSherly' , 'L.M.Muntegmary' , 'A' , True , 12)
b2 = Book('Harry Potter' , 'J.K.Ruling' , 'B' , True , 13)
b3 = Book('Harry Potter' , 'J.K.Ruling' , 'B' , True , 14)

b.addBook()
b2.addBook()
b3.addBook()

b2.removeBook()

m = Member.Members('Nasim' , 18)
m.addMember()
b.rentBook(m)
b2.rentBook(m)


mm = Member.Members('Negar' , 20)
mm.addMember()
b2.rentBook(mm)
b3.rentBook(mm)


# with open('Members' , 'rb') as a:
#     data = pickle.load(a)
# print(data)

mm.getListOfBorrowedBook()
m.getListOfBorrowedBook()

print("-------------")

b2.whoHaveBook()
b3.whoHaveBook()

print("************")

# b2.getInformetionAboutBook()
b3.getInformetionAboutBook()