# class Student:
#     def getStudentDetails(self):
#         self.rollno=input("Enter Roll Number : ")
#         self.name = input("Enter Name : ")
#         self.address =input("Enter Address : ")
#     def printStudentDetails(self):
#         print(self.rollno,self.name, self.address)

# S1=Student()
# S1.getStudentDetails()
# print("\nStudent Details:")
# S1.printStudentDetails()




# class Animal:
#     multicellular = True
#     eukaryotic = True
#     def breathe(self):
#         print("I breathe oxygen.")
#     def feed(self):
#         print("I eat food.")

# class Herbivorous(Animal):
#     def feed(self):
#         print("I eat only plants. I am vegetarian.")
# herbi = Herbivorous()
# herbi.feed()
# # calling some other function
# herbi.breathe()



class Student:
    def __init__(self):
        self.name = ""
        self.roll_no = ""
        self.department = ""
        self.mobile_no = ""
    def read_student_info(self):
        self.name = input("Enter student name: ")
        self.roll_no = input("Enter roll number: ")
        self.department = input("Enter department: ")
        self.mobile_no = input("Enter mobile number: ")
    def print_student_info(self):
        print("\nStudent Information:")
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Department:", self.department)
        print("Mobile Number:", self.mobile_no)
# Create an instance of the Student class
s1 = Student()
# Read and set student information
s1.read_student_info()
# Print student information
s1.print_student_info()

