def check_common(lst1, lst2):
    count = 0
    for i in range(0,len(lst1)):
        for j in range(0,len(lst2)):
            if lst1[i] == lst2[j]:
                count+=1
    return count >= 2

list1 = [1, 2, 3, 10, 5]
list2 = [4, 5, 6, 7, 8]
result = check_common(list1, list2)
if result:
    print("The lists have at least two common members.")
else:
    print("The lists do not have at least two common members.")