class Borrowing_Order:
    def __init__(self, id, date , client_id , book_id , Active ):
        self.__id = id
        self.__date = date
        self.__client_id = client_id
        self.__id_no = book_id
        self.__status = Active

    def get_id(self):
        return self.__id


    def get_status(self):
        return self.__status




