def do_math(num1, num2, operator):
    return num1 + num2 if operator == '+' else num1 - num2

def build_result_list(lst, len_of_longest_element, with_result):
    l = []
    l.append(repr(int(lst[0])).rjust(len_of_longest_element+2))
    l.append(f'{lst[1]}{repr(int(lst[2])).rjust(len_of_longest_element+1)}')
    l.append('-' * (len_of_longest_element + 2))
    if with_result:
        l.append(repr(do_math(int(lst[0]), int(lst[2]), lst[1])).rjust(len_of_longest_element+2))
    return l


def arithmetic_arranger(problems, with_result=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    lst = []
    for problem in problems:

        l = problem.split()
            
        if l[1] not in ['+', '-']:
                return "Error: Operator must be '+' or '-'."
    
        # get longest number
        longest_num = max(len(l[0]), len(l[2]))
        if longest_num > 4:
            return 'Error: Numbers cannot be more than four digits.'
    
        if not l[0].isdigit() or not l[2].isdigit():
            return 'Error: Numbers must only contain digits.'
    
        lst.append(build_result_list(l, longest_num, with_result))

    arranged_problems = ''
    for i in range(0, len(lst[0])):
        for item in lst:
            arranged_problems += f'{item[i]}    '
        arranged_problems = arranged_problems.rstrip()
        if i != len(lst[0])-1:
            arranged_problems += '\n'
            
    return arranged_problems
