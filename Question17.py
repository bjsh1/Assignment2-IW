#17. Write a program that serves as a basic calculator. 
# It asks for two numbers, then it asks for an operator. 
# Gracefully deal with input that doesn't cleanly convert to numbers. Deal with division by zero errors.


num1=int(input("Enter first Number: "))

oper=input("Enter any operator: ")

num2=int(input("Enter Second Number: "))

def calculators(number1,operator,number2):
    if operator=="-":
        return number1-number2

    elif operator=="+":
        return number1+number2

    elif operator=="*":
        return number1*number2

    elif operator=="/":
        
        try:
            return number1/number2
        except ZeroDivisionError:
            print("You can not divide with 0")
    
    elif operator=="%":
        return number1%number2

print(calculators(num1,oper,num2))