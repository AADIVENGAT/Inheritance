#Inheritance:
class Room:
    def __init__(self,len,bth):
       self.len=len
       self.bth=bth

class Hall(Room):
    def get_Area(self):
        print(f"Len:{self.len}\nbth :{self.bth}\nArea of room: {self.len*self.bth}")

r1 = Hall(10,5)        

#r1 = Room(5,5)          
r1.get_Area() 

