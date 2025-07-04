def palindrome(str):
    for i in range (0, int (len (str)/2)):
        if str [i] != str [len (str) -i-1]:
            return False 
        return True

str1 = input("Enter a string:")
ans = palindrome(str1)
if(ans):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome.")
