import itertools

from utils import get_input

def permutation_calc(values: list[int], operator_perm: list[str]) -> int:
    """Apply operators on the values."""
    calc_val = values[0]
    for operator, value in zip(operator_perm, values[1:]):
        if operator == '+':
            calc_val += value
        if operator ==  '*':
            calc_val *= value
        if operator == '||':
            calc_val = int(str(calc_val)+str(value))
    return calc_val


def aoc1():
    puzzle = get_input(day=7)
    data_str = [equation.replace(":", "").split(" ") for equation in puzzle]
    data = [[int(i) for i in equation] for equation in data_str] # data is formatted as list in lists

    sum_equation = 0
    for equation in data:
        operators = ['+', '*']
        length = len(equation[1:])
        operator_perm = [p for p in itertools.product(operators, repeat=length-1)]
        for operator_comb in operator_perm:
            if equation[0] == permutation_calc(equation[1:], operator_comb):
                sum_equation += equation[0]
                break

    return sum_equation

def aoc2():
    puzzle = get_input(day=7)
    data_str = [equation.replace(":", "").split(" ") for equation in puzzle]
    data = [[int(i) for i in equation] for equation in data_str] # data is formatted as list in lists

    sum_equation = 0
    for equation in data:
        operators = ['+', '*', '||']
        length = len(equation[1:])
        operator_perm = [p for p in itertools.product(operators, repeat=length-1)]
        for operator_comb in operator_perm:
            if equation[0] == permutation_calc(equation[1:], operator_comb):
                sum_equation += equation[0]
                break
    return sum_equation

if __name__ == "__main__":
    print("Answer 1:", aoc1())
    print("Answer 2:", aoc2())
