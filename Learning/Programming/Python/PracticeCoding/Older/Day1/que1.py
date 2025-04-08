"""Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321"""


# Code
def descending_order(num):
    # Bust a move right here
    sorted_str = ''.join(sorted(str(num)))
    sorted_str = sorted_str[::-1]
    num = int(sorted_str)
    return num