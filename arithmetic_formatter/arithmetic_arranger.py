def do_math(num1, num2, operator):
    return num1 + num2 if operator == '+' else num1 - num2

def build_result_list(lst, len_of_longest_element, with_result):
    res = []
    res.append(repr(int(lst[0])).rjust(len_of_longest_element+2))
    res.append(f'{lst[1]}{repr(int(lst[2])).rjust(len_of_longest_element+1)}')
    res.append('-' * (len_of_longest_element + 2))
    if with_result:
        res.append(repr(do_math(int(lst[0]), int(lst[2]), lst[1])).rjust(len_of_longest_element+2))
    return res


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

    result = []
    for i in range(0, len(lst[0])):
        result.append('    '.join([item[i] for item in lst]))
    
    arranged_problems = '\n'.join(result)
    return arranged_problems
