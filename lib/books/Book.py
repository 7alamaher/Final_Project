
class Book:
    def __init__(self, id , title , description ,author ,active):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__author = author
        self.status = active

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title
