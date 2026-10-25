from loguru import logger

logger.info("Calculator initialized.")

flag = False



input_lst = []
input_var1 = input("Enter a value ")
# input_lst.append(int(input_var1))
input_operator = input("Enter an operator (+,-,*,/,=) ")
input_var2 = input("Enter next value ")
while(flag== False):
 
    
    if input_var1.isnumeric():
        input_lst.append(int(input_var1))
        input_var1 = " "
    elif input_var2.isnumeric() and input_operator in ["+", "-", "*", "/"]:        
        input_lst.append(input_operator)
        input_lst.append(int(input_var2))
        input_operator = input("Enter an operator (+,-,*,/,=) ")
        input_var2 = " "
    elif input_operator in ["+", "-", "*", "/"]:    
        input_var2 = input("Enter next value ")
    elif input_operator == "=":
        flag = True
    else:
        logger.error("Invalid input. Please enter a numeric value or '=' to quit.")

logger.info(f"Input list: {input_lst}")

for i in range(0, len(input_lst)-1, 2):
    if input_lst[i+1] == "+":
        result = input_lst[i] + input_lst[i+2]
    elif input_lst[i+1] == "-":
        result = input_lst[i] - input_lst[i+2]
    elif input_lst[i+1] == "*":
        result = input_lst[i] * input_lst[i+2]
    elif input_lst[i+1] == "/":
        result = input_lst[i] / input_lst[i+2]
logger.info(f"Result: {result}")

