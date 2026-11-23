#Left-side Right angled triangle
n = int(input("Enter Number"))
for i in range(1 ,n+1):             # i iterates '*'  'n' time (5 rows)
    print('* '*i ,end="\n")         # "*" get multiplied by iterating i (increasing) by every row
