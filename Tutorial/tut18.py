# while loop
# printing the table of 7
# i = 7
# while(i<=70):
#     print(i)
#     i = i + 7

# i = 10
# while(i>=0):
#     print(i)
#     i = i - 1

#Factorial of a Number in Python Using for Loop
# accept input from user
n = int(input("Enter any number: "))

f = 1

# for loop to calculate factorial of a number
for i in range(n, 0, -1):
    f *= i

# print output
print("Factorial is", f)