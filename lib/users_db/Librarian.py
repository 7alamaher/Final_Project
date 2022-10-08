from lib.users_db.Person import Person


class Librarian(Person):

    def __init__(self, id, full_name, age, id_no,full_time,username , password ):

        self.__emplyment_type = full_time
        super(Librarian,self).__init__(id = id, full_name =full_name ,age = age, id_no= id_no,username = username, password=password)



