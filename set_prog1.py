# Find missing and additional values in two lists using set operations.

from loguru import logger

# logger.info("Hello, World!")

list1 = [10, 2, 3, 5]
list2 = [3, 6, 4, 3]

missing_values = []

set_list1 = set(list1)
set_list2 = set(list2)

missing_values_list1 = list(set_list2 - set_list1)
logger.info(f"Missing values in list1: {missing_values_list1}")

# symmetric_difference = set_list1.symmetric_difference(set_list2)
# logger.info(f"Symmetric difference between list1 and list2: {symmetric_difference}")


additional_values_list1 = list(set_list1 - set_list2)
logger.info(f"Additional values in list1: {additional_values_list1 }")

additional_values_list2 = list(set_list2 - set_list1)
logger.info(f"Additional values in list2: {additional_values_list2 }")


