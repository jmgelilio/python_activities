
def addition():
    return first_num + second_num 

def subtraction():
    return first_num - second_num 

def multiplication():
    return first_num * second_num 

def divide():
    return first_num / second_num
    
while True:

    first_num = int(input("Please input first number: "))
    second_num = int(input("Please input second number: "))
    operator = input("Select the operator: ")


    if operator == "+":
        print(addition())
    elif operator == "-":
        print(subtraction())
    elif operator == "/":
        print(divide())
    elif operator == "*":
        print(multiplication())
    else:
        print("Invalid operand")

    next_calculator = input("Do it again? (yes/no)")

    if next_calculator == "no":
        break

else:
    print ("Thank you")