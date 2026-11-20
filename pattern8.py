#Inverted Star Pyramid

n = int(input("Enter Number"))
for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end="")

    for k in range(1,i+1):
        print("*", end=" ")
    print()