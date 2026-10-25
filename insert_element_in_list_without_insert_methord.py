from loguru import logger

index = 0
sample_list = [5,18,77,108,390]
new_element = int(input("Enter a new element to insert into the sorted list: "))

logger.info(f"Original list: {sample_list}")

if not sample_list:
    sample_list.append(new_element)
elif new_element < sample_list[0]:
    sample_list = [new_element] + sample_list
elif new_element > sample_list[-1]:
    sample_list.append(new_element)        
else:
    for i in range(len(sample_list)-1):
        if new_element < sample_list[i]:
            index = i
            break
        else:
            index = len(sample_list)

sample_list.append(None)
for i in range(len(sample_list)-1, index, -1):
    sample_list[i] = sample_list[i-1]
    #sample_list = sample_list[:index] + [new_element] + sample_list[index:]
sample_list[index] = new_element
logger.info(f"Updated list after inserting the new element: {sample_list}")
