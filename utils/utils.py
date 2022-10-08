
class Constatnts:
    Active = 1
    Expired = 2
    Canceled: int = 3





class Method_utils:
    @staticmethod
    def check_value_is_empty(*value:str):
        for item in value:
         if item.isspace() or item == " ":
             return True
