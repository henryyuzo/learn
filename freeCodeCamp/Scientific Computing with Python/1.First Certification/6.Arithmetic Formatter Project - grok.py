# Grok solution to match freeCodeCamp exact output
# Arithmetic Formatter Project

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # Check operators
    for problem in problems:
        if '*' in problem or '/' in problem:
            return "Error: Operator must be '+' or '-'."
    
    # Check digits and extract parts
    num1_list = []
    operator_list = []
    num2_list = []
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Numbers must only contain digits."
        num1, op, num2 = parts
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        num1_list.append(num1)
        operator_list.append(op)
        num2_list.append(num2)
    
    # Build the lines
    top_line = ""
    mid_line = ""
    dash_line = ""
    answer_line = ""
    
    for i in range(len(problems)):
        num1 = num1_list[i]
        op = operator_list[i]
        num2 = num2_list[i]
        width = max(len(num1), len(num2)) + 2  # Space for operator and longest number
        
        # Top line: first number, right-aligned
        top_line += num1.rjust(width)
        # Middle line: operator + space + second number, right-aligned
        mid_line += op + " " + num2.rjust(width - 2)
        # Dash line: dashes matching the width
        dash_line += "-" * width
        
        # Add four spaces between problems, but not after the last one
        if i < len(problems) - 1:
            top_line += "    "
            mid_line += "    "
            dash_line += "    "
    
    # Answers if requested
    if show_answers:
        for i in range(len(problems)):
            num1 = int(num1_list[i])
            num2 = int(num2_list[i])
            op = operator_list[i]
            width = max(len(num1_list[i]), len(num2_list[i])) + 2
            
            if op == '+':
                answer = num1 + num2
            else:  # op == '-'
                answer = num1 - num2
            
            answer_line += str(answer).rjust(width)
            if i < len(problems) - 1:
                answer_line += "    "
        
        return top_line + "\n" + mid_line + "\n" + dash_line + "\n" + answer_line
    else:
        return top_line + "\n" + mid_line + "\n" + dash_line

# Test cases
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))