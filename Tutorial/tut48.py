# Global and Local Variable
x = 10  # global variable


def my_function():
  global x
  x = 5  # this will change the value of the global variable x
  y = 4  # local variable


my_function()
print(x)  # prints 5
# print(y) # this will cause an error because y ide of the function is a local variable and is not accessible outside