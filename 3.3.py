list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [num for num in list2 if num not in list1]
print(list3)