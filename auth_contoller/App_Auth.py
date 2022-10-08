from typing import List
import librarian as librarian
from lib.books.Borrowing_Order import Borrowing_Order
from lib.books.Book import Book
from lib.users_db.Client import Client
from lib.users_db.Librarian import Librarian
from utils import utils
from utils.utils import Constatnts


class App_Auth:

    librarians_list:list[librarian] = [Librarian(id=1, full_name="hala", age=22, id_no=2234,full_time=True,username="7ala" , password="123"),
                                       Librarian(id=2, full_name="farah", age=25, id_no=3324, full_time=True,username="farah", password="321"),
                                       Librarian(id=3, full_name="layan", age=34, id_no=4432, full_time=True,username="layan", password="213"),
                                       Librarian(id=4, full_name="noor", age=22, id_no=2234,full_time=True,username="noor" , password="231")]

    Client_list: list[Client] = [Client(id=1, full_name="mohamad", age=18, id_no=223,phone_number="05932167",username="mohamad" , password="987"),
        Client(id=2, full_name="sami", age=23, id_no=332,phone_number="059439217",username="sami" , password="789"),
        Client(id=3, full_name="rana", age=19, id_no=443,phone_number="05932188",username="rana" , password="879" ),
        Client(id=4, full_name="sona", age=20, id_no=223,phone_number="05982356",username="sona-" , password="897")]

    Book_list:list[Book] = [Book(id=1 , title="Harry Potter" , description="majic film" ,author="J. K. Rowling" ,active=True),
                            Book(id=2 , title="Little Women" , description="fantactice film" ,author="Louisa May Alcott" ,active=True)]


    Borrowed_orders_list: list[Borrowing_Order] = [Borrowing_Order(id=1,date= "5/10/2022" ,client_id= 2 ,book_id = 1,book_title="Harry Potter", Active=1),
                                                   Borrowing_Order(id=2, date="7/9/2022", client_id=3, book_id=2,book_title="Little Women",Active=1)]


    def get_last_id(self)->int:
      return self.Client_list[len(self.Client_list) - 1].get_id()



    def login (self , username:str , password:str) -> bool:
        for item in self.librarians_list:
            if username == item.get_username() and password == item.get_password():
                return True

        return False

    def register_new_user (self , user:librarian ):
       if not self.check_if_user_exsiest(username=user.get_username()):

           self.librarians_list.append(user)

       else:
            print("User already Used!")

    def register_new_user_client(self, user: Client):
        if not self.check_if_user_exsiest(username=user.get_username()):
            self.Client_list.append(user)

        else:
            print("User already Used!")
            print(len(self.Client_list))

    def check_if_user_exsiest(self,username:str):
        for item in self.librarians_list:
            if item.get_username() == username :
                return True
        return False
    def check_if_book_exsiest(self,title:str):
        for item in self.Book_list:
            if item.get_title() == title :
                return True
        return False

    def register_new_book(self, book: Book):
        if not self.check_if_book_exsiest(title=book.get_title()):
            self.Book_list.append(book)

        else:
            print("Book is already append!")
            print(len(self.Book_list))

    def show_avalible_book(self)->List[str]:
        active_titles:List[str] = []
        for item in self.Borrowed_orders_list:
           if item.get_status() == Constatnts.Active:
              active_titles.append(item.get_title())
              return active_titles

    def register_new_borrowing_order(self, borrowing_order: Borrowing_Order):
      self.Borrowed_orders_list.append(borrowing_order)

    def check_if_brrowwing_id_exsiest(self, id:int):
        for item in self.Borrowed_orders_list:
            if item.get_id() == id:
                return True
        return False