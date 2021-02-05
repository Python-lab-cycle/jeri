from Graphics.rectanglefunction import*
from Graphics.circlefunction import*
from Graphics.DGraphics.cuboidfunction import*
from Graphics.DGraphics.spherefunction import *
radius=int(input("enter radius"))
print("area of circle=",circlearea(radius))
print("perimeter of circle=",circleperimeter(radius))


length=int(input("enter length of rectangle"))
breadth=int(input("enter the breadth"))
print("area of rectangle=",rectanglearea(length,breadth))
print("perimeter of rectangle=",rectangleperimeter(length,breadth))

length=int(input("enter length of cuboid"))
breadth=int(input("enter the breadth"))
height=int(input("enter the height"))
print("perimeter of cuboid=",cuboidarea(length,breadth,height))
print("area of cuboid=",cuboidperimeter(length,breadth,height))
   
radius=float(input("enter radius of sphere"))
print("area of sphere=",spherearea(radius))
print("perimeter of sphere=",sphereperimeter(radius))
