# Find the common elements in 3 sorted list using set and loop with list both methods.

from loguru import logger

arr1 = [1,5,10,20,40,80]
arr2 = [6,7,20,80,100]
arr3 = [3,4,15,20,30,70,80,120]

set1 = set(arr1)
set2 = set(arr2)
set3 = set(arr3)

common_elements = set1.intersection(set2).intersection(set3)
# logger.info(f"Common elements in all three lists: {common_elements}")   

#seccond method using loop and list

common_lst = []

for item in arr1:
    if item in arr2 and item in arr3:
        common_lst.append(item)
    else:
        continue


logger.info(f"Common list elements in all three lists: {common_lst}")   
