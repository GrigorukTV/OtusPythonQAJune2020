from classes import Triangle, Square, Rectangle, Circle

squa = Square('Square1', 1, 7)
triang = Triangle('Triangle', 2, 8)
rect = Rectangle('Rectangle', 3, 8)
circ = Circle('Circle', 4, 8)



s = squa.add_square(circ)
t = triang.add_square(squa)
r = rect.add_square(triang)
c = circ.add_square(rect)

squa.getAngles()

print(squa.name)

squa.setName('test')
print(s)