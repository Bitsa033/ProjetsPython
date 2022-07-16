from ClasseRobot import Robot

r = Robot()
r.changeOrientation("N")
r.changeX(15)
r.changeY(8)

ori = r.o
x = r.x
y = r.y

coordonnees = "({},{})({})".format(x, y, ori)

print(coordonnees)
