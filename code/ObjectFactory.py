from code.Constants import OBJECT_NAME
from code.Food import Food
from code.Item import Item


class ObjectFactory:

    @staticmethod
    def create_object(object_name : str, position : tuple):
        food_names = OBJECT_NAME[:6]
        if object_name in food_names:
            return Food(object_name, position)
        else:
            return Item(object_name, position)