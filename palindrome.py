a = input("Enter the string to check its palindrome: ")
a = a.lower()
if (a == a[::-1]):
    print("Palindrome")
else:
    print("Not palindrome")