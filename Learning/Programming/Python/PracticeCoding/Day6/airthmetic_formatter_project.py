# Build an Arithmetic Formatter Project

"""
problem Link:- https://www.freecodecamp.org/learn/scientific-computing-with-python/build-an-arithmetic-formatter-project/build-an-arithmetic-formatter-project



"""
def arithmetic_arranger(problems, show_answers=False):
    if len(problems)>5:
        return 'Error: Too many problems.'
    
    first_line = []
    second_line = []
    dashes = []
    res =  []
    valid_operators = {'+','-'}
    for problem in problems:
        parts = problem.split()
        a,b,c = parts[0],parts[1],parts[2]
        if b not in valid_operators:
            return "Error: Operator must be '+' or '-'."
        if not (a.isdigit() and c.isdigit()):
            return 'Error: Numbers must only contain digits.'
        if len(a)>4 or len(c)>4:
            return 'Error: Numbers cannot be more than four digits.'
        lengt = max(len(a),len(c)) +2
        first_line.append(a.rjust(lengt))
        second_line.append(b +" "+ c.rjust(lengt-2))
        dashes.append("-"*lengt)
        if show_answers:
            res.append(str(eval(a + b + c)).rjust(lengt))

    # Join the formatted output with exactly 4 spaces between each column
    arranged_problems = "\n".join([
        "    ".join(first_line),
        "    ".join(second_line),
        "    ".join(dashes)
    ])
    if show_answers:
        arranged_problems += "\n" + "    ".join(res)
    # problems = arranged_problems
    return arranged_problems

print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')

'''

# **Test Cases**
test_cases = [
    (["3801 - 2", "123 + 49"], False),
    (["1 + 2", "1 - 9380"], False),
    (["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], False),
    (["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"], False),
]

for i, (problems, show_answers) in enumerate(test_cases, 1):
    print(f"\nTest Case {i}:\n{arithmetic_arranger(problems, show_answers)}\n")

'''