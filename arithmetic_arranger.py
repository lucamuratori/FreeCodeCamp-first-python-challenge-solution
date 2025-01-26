def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # problem-splitting list
    problem_list = [i.split(' ') for i in problems]

    # Variables
    first_operand_list = []
    second_operand_list = []
    lines_list = []
    answers = []

    # Error-checking loop
    for problem in problem_list:
        # Checking that all operands are decimal
        if problem[0].isdecimal() and problem[2].isdecimal():

            # Checking all numbers to be 4 or less digits
            if len(problem[0]) > 4 or len(problem[2]) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            
            # Checking operators to be only + or -
            if problem[1] != '+' and problem[1] != '-':
                return "Error: Operator must be '+' or '-'."
            
            # Get the total length of the operation
            distance = max(len(problem[0]), len(problem[2])) + 2
        
            # Compiling the first line
            first_operand_list.append(str(problem[0].rjust(distance)) + '    ')
            # Compiling the second line
            second_operand_list.append((str(problem[1])) + (str(problem[2])).rjust(distance - 1) + '    ')

            # Compiling the lines
            lines_list.append(str('-' * distance + '    '))
            
            # Calculating answers only if show_answers is passed True
            if show_answers:
                if problem[1] == '+':
                    answers.append(str(int(problem[0]) + int(problem[2])).rjust(distance) + '    ')
                    
                else:
                    answers.append(str(int(problem[0]) - int(problem[2])).rjust(distance) + '    ')
                    
                
            
        else:
            return 'Error: Numbers must only contain digits.'
        
    if show_answers:
        problems = ''.join(first_operand_list).rstrip() + '\n' + ''.join(second_operand_list).rstrip() + '\n' + ''.join(lines_list).rstrip() + '\n' + ''.join(answers).rstrip()
    else:
        problems = ''.join(first_operand_list).rstrip() + '\n' + ''.join(second_operand_list).rstrip() + '\n'  + ''.join(lines_list).rstrip()
    return problems

print(arithmetic_arranger(["32 - 698", "3801 - 2", "45 + 43", "123 + 49"]))