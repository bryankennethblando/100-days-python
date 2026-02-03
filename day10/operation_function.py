# Functions of the calculator

def operation(input_one, input_two, selected_operation):
    if selected_operation == "+":
        result = input_one + input_two
        return f"the answer is: {result}"
    
    elif selected_operation == "-":
        result = input_one - input_two
        return f"the answer is: {result}"
    
    elif selected_operation == "*":
        result = input_one * input_two
        return f"the answer is: {result}"
    
    elif selected_operation == "/":
        result = float(input_one) / float(input_two)
        return f"the answer is: {result}"

    elif selected_operation == "%":
        result = input_one % input_two
        return f"the answer is: {result}"
        