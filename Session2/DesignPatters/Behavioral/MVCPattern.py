class Model:
    book = [{'maghaze_khod_koshi': {'price': 100}},
            {'anneh_sher_li': {'price': 150}},
            {'aghayed_ye dalghak': {'price': 250}}]


class View:
    def book_list(self, bookList):
        for book in bookList:
            for i in book:
                print(i)

    def book_price(self, bookList):
        for book in bookList:
            for bookname, val in book.items():
                print("{} gheymatedh inghade {}".format(
                    bookname, val['price']))


class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model()
        self.bookList = self.model.book

    def show_book_list(self):
        self.view.book_list(self.bookList)

    def show_book_price(self):
        self.view.book_price(self.bookList)


class Client:
    def __init__(self):
        self.controller = Controller()
        self.controller.show_book_list()
        self.controller.show_book_price()


if __name__ == "__main__":
    client = Client()