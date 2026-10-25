from loguru import logger

index = 0
lst = [202,165,89,76,12]
flag = False

new_element = int(input("Enter a new element to insert into the sorted list: "))    

logger.info(f"Original list: {lst}")

if not lst:
    lst.append(new_element)
elif new_element > lst[0]:
    lst = [new_element] + lst
elif new_element < lst[-1]:
    lst.append(new_element)    
else:
    flag = True
    lst.append(None)
    for i in range(len(lst)-1):
        if new_element > lst[i]:
            index = i
            break
        else:
            index = len(lst)        

logger.info(f"list after inserting the new element: {lst}")

if flag == True:
    for i in range(len(lst)-1, index, -1):
        lst[i] = lst[i-1]
        #lst = lst[:index] + [new_element] + lst[index:]

logger.info(f"Updated list after inserting the new element: {lst}")



if index != 0 and index != len(lst)-1:    
    lst[index] = new_element

logger.info(f"Updated list after inserting the new element: {lst}")

