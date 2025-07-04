# a = input("Enter the Number:")
# print(f"The multiplication table of {a} is:")

# try:
#  for i in range(1, 11):
#     print(f"{int(a)} X {i} = {int(a)*i}")

# except Exception as e:
#              print(e)
# except:
#     print("Invalid Input")

# print("some imp lines are executed")
# print("end of code")


try:
    num=int(input("Enter an Integer: "))
    a = [6, 3]
    print(a[num])

except ValueError:
    print("Entered value is not an integer")

except IndexError:
    print("Index Error") 