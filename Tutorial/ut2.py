# try:
#     num = int(input("Please enter number:"))
#     if num < 0:
#         raise ValueError()

# except ValueError:
#     print("Number is negative")
#     print("ValueError Exception thrown")




def con(str1, str2):
    return str1 + str2

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

concate = con(string1, string2)
print("Concatenated string:", concate)



# class Student:
#     def __init__(self, name, department, roll_no):
#         self.name = name
#         self.department = department
#         self.roll_no = roll_no

#     def read(self):
#         self.name = input("Enter student's name: ")
#         self.department = input("Enter student's department: ")
#         self.roll_no = input("Enter student's roll number: ")

#     def display(self):
#         print("\nStudent Information:")
#         print("Name:", self.name)
#         print("Department:", self.department)
#         print("Roll Number:", self.roll_no)
#         print("\n")

# student1 = Student("John Doe", "Computer Science", "07")
# student1.display()
# student1.read()
# student1.display()



# overriding
# class Parent():  
# 	def __init__(self): 
# 		self.value = "Inside Parent"

# 	def show(self): 
# 		print(self.value) 

# class Child(Parent): 
# 	def __init__(self):     
# 		self.value = "Inside Child"

# 	def show(self): 
# 		print(self.value) 

# obj1 = Parent() 
# obj2 = Child() 

# obj1.show() 
# obj2.show() 
