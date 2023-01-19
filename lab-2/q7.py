# 2. Pattern Printing
def prtPattern():
    n=int(input("Enter number of rows: "))
    for i in range(1, n+1, 1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

prtPattern()