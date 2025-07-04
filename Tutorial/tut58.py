# class Emp:
#     def __init__(self):
#         name = print(input("Enter a Name:\t"))
#         sal = int(input("Enter a Salary:\t"))
#         dept = print(input("Enter a Department:\t"))
#         print(f"{self.name} is working in {self.dept} department with salary {self.sal}")

# a = Emp()

class Person:

  def __init__(self, name, occ):  # here the self argument is automatically passes through the object
    print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")

a = Person("Atharva", "Developer")
b = Person("Divya", "HR") 
a.info()
b.info()
# print(a.name)
# a.name = "Divya"
# a.occ = "HR"
# a.info()
