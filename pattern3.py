#Left-side Inverted Right-angled Triangle
n = int(input("Enter Number"))
for i in range(n, 0, -1):           #loops runs from 5-0 by step(-1)
    print('* '*i ,end=" \n")        # "*" get multiplied by iterating i (decreasing) by every row