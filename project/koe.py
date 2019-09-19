class Cow:

    def __init__(self, weight, age):
        self.weight = weight  
        self.age = age
    def myfunc():
        global x
        x = "0,1,2,3,4"    
           
class Feed:

    def __init__(self, koe):
        if koe.weight == 450 and koe.age == 0:
            self.energy = 26500 
            self.protein = 215
        elif koe.weight == 500 and koe.age == 0:
            self.energy = 29500
            self.protein = 245
        elif koe.weight == 575 and koe.age == 0:
            self.energy = 31500
            self.protein = 255  
        elif koe.weight == 600 and koe.age == 0:
            self.energy = 37000
            self.protein = 305
        elif koe.weight == 650 and koe.age == x:
            self.energy = 40000*(1-(0.05)*x)
            self.protein = 350*(1-(0.05)*x)
        

