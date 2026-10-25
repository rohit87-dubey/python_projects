from loguru import logger

name = "rohit Dubey"
dict1={}
for char in name:
    if char in dict1:
        dict1[char] += 1
    else:
        dict1[char] = 1

logger.info(f"Character count in the name '{name}': {dict1}")

