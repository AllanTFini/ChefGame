from code.Object import Object


class Food(Object):
    def __init__(self, name : str, position : tuple):
        super().__init__(name, position)