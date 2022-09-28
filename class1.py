class Circle:
    #class variable
    pi=3.14159
    
    #constructor
    def __init__(self,radius):
        #instance variable
        self.radius=radius
        
    #method
    def area(self):
        a = Circle.pi*self.radius*self.radius
        print("Area of circle=",a)
        
#creating object
c = Circle(5)
#invoking method
c.area()