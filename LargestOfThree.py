a,b,c = input("enter numbers separated by spaces : ").split(" ")
a = int(a)
b = int(b)
c = int(c)
if a > b and a > c:
    print(f"Largest : {a}")
elif b > a and b > c:
    print(f"Largest : {b}")
else:
    print(f"Largest : {c}")