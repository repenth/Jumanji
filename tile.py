class Tile:
    def __init__(self, xCoordinate, yCoordinate):  
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate

    def say_hi(self):  
        print('Hello, tile: x: '+ str(self.xCoordinate)+" y: "+ str(self.yCoordinate))
