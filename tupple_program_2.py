from loguru import logger

tuple1= (10,2,3,5)
tuple2= (3,6,4,3)

output_lst = []
# output should be the power of the first tuple to the second tuple
# result = tuple(a ** b for a, b in zip(tuple1, tuple2))
for a, b in zip(tuple1, tuple2):
    result = a ** b
    output_lst.append(result)

logger.info(f"Result: {tuple(output_lst)}")
