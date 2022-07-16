class Robot:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.o = "N"

    def changeOrientation(self, orientation):
        self.o = orientation

    def changeX(self, x):
        self.x = x

    def changeY(self, y):
        self.y = y

    def deplacerRobot(self, orientation):
        if orientation == self.o:
            self.y += 1
