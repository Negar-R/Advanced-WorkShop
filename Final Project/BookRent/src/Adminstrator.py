import sqlite3
import BookList

cursorA = BookList.Member.conn.cursor()

class Admin():
    def __init__(self):
        pass

    def getInformetionAboutBook(self , bookId):

        BookList.cursorB.execute("SELECT * FROM books WHERE BOOKID = ?" , (bookId ,))
        s = BookList.cursorB.fetchall()

        for i in s:
            print(s)

    def getListOfBorrowedBook(self , iD):  

        cursorA.execute("SELECT BORROWEDBOOK FROM members WHERE ID = ?" , (iD ,))
        s = cursorA.fetchall()
        
        print(s)


# b = BookList.Book('OnSherly' , 'L.M.Muntegmary' , 'A' , True , '12' , 1)
# b2 = BookList.Book('Harry Potter' , 'J.K.Ruling' , 'B' , True , '13' , 2)
# b3 = BookList.Book('Harry Potter' , 'J.K.Ruling' , 'c' , True , '14' , 2)

# b.addBook()
# b2.addBook()
# b3.addBook()

# b2.getInformetionAboutBook()
# b3.getInformetionAboutBook()

a = Admin()
# m.getListOfBorrowedBook('12')
a.getInformetionAboutBook('12')

print("***********")

# a.rentBook('9751bbba-1fcc-11ea-b430-5fe9d1ad5d5b' , 12)
