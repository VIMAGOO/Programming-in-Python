class Rectangle:
   def __init__(self, llargada, amplada):
       self.llargada = llargada
       self.amplada = amplada

class Triangle:
   def __init__(self, llargada, amplada):
       self.llargada = llargada
       self.amplada = amplada

def area_rectangle(rect):
    return rect.llargada * rect.amplada

def test():

   rectangle = Rectangle(3,6)
   assert area_rectangle(rectangle) == 18

   triangle = Triangle(3,6)
   assert area_rectangle(triangle) == 18