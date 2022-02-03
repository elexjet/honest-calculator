 # Flowchart Stage 5/5 Final Working
msg_0 = "Enter an equation" 
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

memory = 0.0
result = 0.0

def flow_chart():
    global memory
    x, operator, y = input(msg_0).split()    # Print msg_0 and split calc into two variables 
    if x == "M":
        x = memory
    if y == "M":
    # elif y == "M":
        y = memory
    else:
        pass
    first_calculations(x, operator, y)

def first_calculations(x, operator, y):
    global result
    operators = "+-*/"
    try:
        if operator not in operators:
            print(msg_2)
            flow_chart()
        else:
            x = float(x)    # Test if x is a float or int
            y = float(y)    # Test if y is a float or int
            
            check(x, y, operator)
            if operator == "+":
                result = x + y
            
            elif operator == "-":
                result = x - y
            
            elif operator == "*":
                result = x * y
            
            elif operator == "/":
                if y == 0.0:  # Test for y = 0 for division by zero violation
                    print(msg_3)
                    flow_chart()
                    return 
                else:
                    result = x / y
            print(result)                       
            total_recall()
                
    except ValueError:
        print(msg_1)
        flow_chart()        

def total_recall():
    global result, memory
    print(msg_4)
    answer_one = input()
    # while True:
    if answer_one == "y":
        memory = saving_memory(result, memory)
    elif answer_one == "n":
        pass
    message_five()

def message_five():
    print(msg_5)
    answer_two = input()
    if answer_two == "y":
        flow_chart()
    elif answer_two == "n":
        exit()    # print None as temporary test

def check(x, y, oper):
    msg = ''
    if is_one_digit(x) and is_one_digit(y):
        msg = msg + msg_6
    if (x == 1 or y == 1) and oper == "*":
        msg = msg + msg_7
    if (x == 0 or y == 0) and (oper == "*" or oper == "+" or oper == "-"):
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)
    return msg

def is_one_digit(x):
    #########
    if x.is_integer():
        x = int(x)
        
    #########
    if -10 < x and x < 10 and isinstance(x, int):
        output = True
    else:
        output = False
    return output
    
def saving_memory(result, memory):
    msg_ = [i for i in range(10)]
    msg_.append(msg_10)
    msg_.append(msg_11)
    msg_.append(msg_12)
    
    if is_one_digit(result):
        msg_index = 10
        while True:
            print(msg_[msg_index])
            answer_three = input()
            if answer_three == "y":
                if msg_index < 12:
                    msg_index += 1
                else:
                    memory = result
                    break
            elif answer_three == "n":
                break
    else:
        memory = result
    return memory
    
if __name__ == "__main__":
    flow_chart()