l= []
ele=0
total=0
n = int(input("Enter number of elements : "))
for i in range(0, n):
    print("Enter elements:")
    ele = int(input()) 
    l.append(ele)
print(l)
for ele in range(0, n): 
    total = total + l[ele] 
print("Sum of all elements in the list: ", total)