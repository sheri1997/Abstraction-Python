from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def totalsides(self):
        pass

class Triangle(Polygon):
    def totalsides(self):
        print("3 Sides")

class Pentagon(Polygon):
    def totalsides(self):
        print("5 Sides")

class Hexagon(Polygon):
    def totalsides(self):
        print("6 Sides")


sides_triangle = Triangle()
sides_triangle.totalsides()

sides_pentagon = Pentagon()
sides_pentagon.totalsides()

sides_hexagon = Hexagon()
sides_hexagon.totalsides()
