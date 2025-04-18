n = int(input("enter number to find it's factorial: "))
que = n
fact = 1
while n > 1:
    fact *= n
    n -= 1
print(f"Factorial of {que} is {fact}")