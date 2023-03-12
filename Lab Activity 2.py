Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Circle:
...     pi = 3.14159
...     
...     def __init__(self, radius):
...         self.radius = radius
...     
...     def Perimeter(self):
...         return 2 * Circle.pi * self.radius
...     
...     def Area(self):
...         return Circle.pi * self.radius ** 2
...     
...     def Display(self):
...         print("Perimeter:", self.Perimeter())
...         print("Area:", self.Area())
... 
... radius = float(input("Enter the radius of the circle: "))
... circle = Circle(radius)
