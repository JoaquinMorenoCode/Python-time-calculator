

class Rectangle:
    
    width = 0
    height = 0
    
    def __init__(self, width : int, height : int) :
        self.width = width
        self.height = height
    
    def set_width(self, width : int):
        self.width = width
         
        
    def set_height(self, height : int):
        self.height = height
        
        
    def get_area(self):
        return(self.height * self.width)
    
    def get_perimeter(self):
        return((self.height * 2) + (self.width * 2))
    
    def get_diagonal(self):
        return((self.width**2 + self.height**2)**.5)
    
    def get_picture(self):
        
        if(self.width > 50 or self.height > 50):
            return("Too big for picture.")       
        
        column = []        
        
        for i in range(self.height):
            for i in range(self.width):
                column.append("*")

            column.append("\n")
        return  "".join(column)
    
    def get_amount_inside(self,shape : "Rectangle"):
        
        # if(self.get_area()<shape.get_area()):
        #     return 0
        return  int(self.get_area()/ shape.get_area())
    
    
    def __str__(self) -> str:
        return "Rectangle(width={}, height={})".format(self.width,self.height)
 
class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)
        
    def set_side(self,side):
        self.set_height(side)
        self.set_width(side)
        
    def set_width(self, side : int):
        self.width = side
        
    def set_height(self, side : int):
        self.height = side
        
    def __str__(self) -> str:
        return "Square(side={})".format(self.width)
   
            
    