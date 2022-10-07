#objects are created using the
#the class describes what the object will be
#the class can be described as the object of the class.
#class are created with the key word class and intended block which contain class method(methods are functions).
#the __init__ method is the most important method(function) in a class
# the function is called when the instance(object) of the class is crreated using the name of function as the class
# every method of a class must have self as the first parameter
# self refer to the instances calling the method
#the __init__ the thod is the class costructor

class cat:
    def __init__(self, color, legs):
     self.color = color
     self.legs = legs

black=cat("spotted", 4)
white=cat("black", 6)
mwizi=cat("red", 4)
print( white.color,white.legs, 
      black.color, black.legs,
      mwizi.color,mwizi.legs) 