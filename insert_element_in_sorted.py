from loguru import logger
# print("hello")
# logger.info("This is an info message")

sample_list = [5,18,77,108,390]
logger.info(f"Original list: {sample_list}")
logger.info("Enter a new element to insert into the sorted list: ")
new_element = int(input())
logger.info(f"New element entered: {new_element}")
for i in range(len(sample_list)):
    if new_element < sample_list[i]:
        sample_list.insert(i,new_element)
        break
    else:
        continue

logger.info(f"Updated list after inserting the new element: {sample_list}")


