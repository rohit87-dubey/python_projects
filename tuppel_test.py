from loguru import logger

new_tupple = ([1,2,3],[4,5,6],[6,7])
new_lst = []
for lst in new_tupple:
    new_lst = new_lst + lst

print(tuple(new_lst))

