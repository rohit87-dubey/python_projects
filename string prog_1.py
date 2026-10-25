# swapcase the string without using the swapcase() method
from loguru import logger

str_var1 = "Hello World"
str_var2 = ""
for char in str_var1:
    if char.islower():
        str_var2 = str_var2 + char.upper()
        # logger.info(char.upper(), end="")
    elif char.isupper():
        str_var2 = str_var2 + char.lower()
        # logger.info(char.lower(), end="")
    else:
        # logger.info(char, end="")
        str_var2 = str_var2 + char
        continue

logger.info(str_var2)
