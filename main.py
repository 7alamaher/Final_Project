from auth_contoller.App_Auth import App_Auth
from lib.books.Book import Book
from lib.books.Borrowing_Order import Borrowing_Order
from lib.users_db.Client import Client
from lib.users_db.Librarian import Librarian
from utils.utils import Method_utils
from utils.utils import Constatnts
def get_input_from_user_client(app_auth:App_Auth ):
   full_name = input("Enter Client name:")
   age = input("Enter Client age:")
   phone_number = input("Enter Client phone_number :")
   id_no = input("Enter Client id_no:")

   if Method_utils.check_value_is_empty(username, age , phone_number , id_no):
      print("Invaild inputs")
      return

   client = Client(full_name=full_name, age = age , phone_number=phone_number, id_no=id_no,id = auth.get_last_id()+1,username=username, password=password)
   app_auth.register_new_user(client)

def get_input_from_user_Librarian(app_auth:App_Auth ):
   full_name = input("Enter Librarian name:")
   age = input("Enter Librarian age:")
   id_no = input("Enter Librarian id_no:")
   emplyment_type= input("Enter Librarian emplyment_type(1-full_time/2-part_time):")

   if Method_utils.check_value_is_empty(username, age , id_no,emplyment_type):
      print("Invaild inputs")
      return

   librarian = Librarian(full_name=full_name, age = age ,full_time= True, id_no=id_no,id = auth.get_last_id()+1,username=username, password=password)
   app_auth.register_new_user(librarian)

def get_input_from_user_Book(app_auth:App_Auth ):
   title = input("Enter Book  title:")
   author = input("Enter Book author:")
   description = input("Enter Book description :")
   status = input("Enter Book status(1-Active/2-Inactive):")

   if Method_utils.check_value_is_empty( title, author , description ,  status):
      print("Invaild inputs")
      return

   book = Book( title= title, author = author , description=description,active= True ,id = auth.get_last_id()+1)
   app_auth.register_new_book(book)

def get_input_from_user_Borrowing_Order(app_auth: App_Auth):
         id = input("Enter Borrowing_Order id:")
         date= input("Enter Borrowing_Order data:")
         client_id= input("Enter Borrowing_Order client_id :")
         book_id= input("Enter Borrowing_Order book_id:")
         book_title = input("Enter Borrowing_Order book_title:")

         if Method_utils.check_value_is_empty(id, date , client_id , book_id ,book_title):
            print("Invaild inputs")
            return

         borrowing_order = Borrowing_Order(book_title=book_title , date= date,  client_id= client_id,  book_id= book_id, id=auth.get_last_id() + 1, Active = Constatnts.Canceled )
         app_auth.register_new_borrowing_order(borrowing_order)



print("Welcome , please add your credential: ")
username = input("username :")
password = input("password:")

if Method_utils.check_value_is_empty(username , password) :
   print("Empty fileds")
   exit()

auth = App_Auth()


if auth.login(username,password):
   print("What you want to do: \n 1-Add new Client.\n2- Add new librarian\n3_Add new Book\n4_ Ask to borrow a book\n5_Return book to librarian ")

   use_choice = input("user choice:")
   if not Method_utils.check_value_is_empty(use_choice):
      if use_choice == "1":
       get_input_from_user_client(auth)

      elif use_choice == "2":
         get_input_from_user_Librarian(auth)

      elif use_choice == "3":
        count = 0
        str_books = input("Enter numer of books you want to borrow :")
        if str_books.isdigit() and str_books != "":
           num_of_books = int (str_books)
           while count < num_of_books  :
               get_input_from_user_Book(auth)
               count += 1

      elif use_choice == "4":
         for item in auth.show_avalible_book() :
          print(item)

         id_no = input("Enter Client id_no:")
         if Method_utils.check_value_is_empty(id_no):
           print("Invaild inputs")

         elif not auth.check_if_user_exsiest(id_no):
           get_input_from_user_Borrowing_Order(auth)
           print("Book has been borrowed")

      elif use_choice == "5":
          borrowing_id = int(input("Enter brrowwing_id to return book:"))
          if auth.check_if_brrowwing_id_exsiest(borrowing_id):
              for item in auth.Borrowed_orders_list:
                  if item.get_id() == borrowing_id:
                      item.set_status(Constatnts.Active)
                      print("Book has been returned",item.get_status())
















