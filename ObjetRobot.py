from ClasseRobot import Robot

print("Programme python qui simule le deplacement d'un robot")
r = Robot()
r.changeOrientation("N")
r.changeX(15)
r.changeY(8)
r.changeX(6)
r.changeY(12)
r.changeX(1)
r.changeX(1)
r.changeOrientation("S")

ori = r.o
x = r.x
y = r.y

coordonnees = "({},{})({})".format(x, y, ori)

print(coordonnees)
