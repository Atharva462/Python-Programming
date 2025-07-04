def swap(a, b):
    temp = a
    a = b
    b = temp
    print("After Swapping")
    print("a",a)
    print("b",b)

a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
print("Before Swapping")
print("a",a)
print("b",b)
swap(a, b)
