from lib.users_db.Person import Person


class Client(Person) :
    def __init__(self,id,full_name,age,id_no,phone_number,username , password ):

        self.__phone_number = phone_number
        super(Client,self).__init__(id = id, full_name =full_name ,age = age, id_no= id_no,username = username, password=password)


    def get_phone_number(self):
        return self.__phone_number
