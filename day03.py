import re
import functools

from utils import get_input

def multiply(mul_str: str):
    """Input is regex in the form 'mul(d+, d+)' and returns multiplication of the values."""
    numbers = re.findall('\d+', mul_str)
    reduced = functools.reduce( lambda a,b : int(a)*int(b) , numbers) # cumulative operations on iterables
    return reduced

def aoc1():
    computer_memory = get_input(day=3, as_list=False)
    occurences = re.findall('mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)', computer_memory)
    multiplied_num = []
    for occurence in occurences:
        multiplied_num.append(multiply(occurence))
    result = sum(multiplied_num)

    return result

def aoc2():
    computer_memory = get_input(day=3, as_list=False)

    multiplied_num = []
    enabled = True
    for operator, value1, value2, dont, do in re.findall("(mul)\(([1-9][0-9]{0,2}),([1-9][0-9]{0,2})\)|(don't\(\))|(do\(\))", computer_memory):
        if do:
            enabled = True
        elif dont:
            enabled = False
        elif enabled and operator:
            number = int(value1) * int(value2)
            multiplied_num.append(number)
    result = sum(multiplied_num)
    return result

if __name__ == "__main__":
    print("Answer 1:", aoc1())
    print("Answer 2:", aoc2())
