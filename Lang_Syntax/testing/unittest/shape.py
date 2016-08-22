class Shape:

    
    def __init__(self):
        self.shapes = {}


    def add(self, shape, desc):
        self.shapes[shape] = desc


    def get(self, shape):
        assert shape != None, "shape parameter is required!"
        return self.shapes[shape]

