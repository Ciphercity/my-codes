#how to create a class with objects
class student:
    def __init__(self,name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

student1=student( "junior", "light skin", 65)
student2=student( "tom","dark skin", 78)
print (student2.name, student2.color, student2.weight)
print (student1. name, student1. color, student1. weight)
    