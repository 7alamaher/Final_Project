
class Person :
    def __init__(self, id, full_name, age, id_no, username="", password=""):
        self.__id = id
        self.__full_name = full_name
        self.__age = age
        self.__id_no = id_no
        self.__username = username
        self.__password = password

    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password