n = int(input("Enter the number : "))
if n <=1 :
    print("0")
else:
    for i in range(2,n+1,2):
        print(i,end=", ")