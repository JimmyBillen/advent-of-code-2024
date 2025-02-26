from utils import get_input

def is_ordered(update: list, rules: list) -> bool:
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if not update.index(rule[0]) < update.index(rule[1]):
                return False
    return True

def prepare_data(data):
    rulelines, updatelines = data.split("\n\n")

    rules = []
    for rule in rulelines.splitlines():
        rules.append( [int(num) for num in rule.split('|')] )

    updates = []
    for update in updatelines.splitlines():
        updates.append([int(p) for p in update.split(',')])
    return rules, updates

def make_ordered(update: list, rules: list) -> list:
    while not is_ordered(update, rules):
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                index_rule1 = update.index(rule[0])
                index_rule2 = update.index(rule[1])
                if not index_rule1 < index_rule2:
                    update[index_rule1], update[index_rule2] = update[index_rule2], update[index_rule1]
    return update

def aoc1():
    data = get_input(day=5, as_list=False)

    rules, updates = prepare_data(data)

    score = 0
    for update_check in updates:
        if is_ordered(update_check, rules):
            middle_value = update_check[len(update_check)//2]
            score += middle_value
    return score

def aoc2():
    data = get_input(day=5, as_list=False)

    rules, updates = prepare_data(data)

    not_ordered_updates = []
    for update_check in updates:
        if not is_ordered(update_check, rules):
            not_ordered_updates.append(make_ordered(update_check, rules))
    
    score = 0
    for update in not_ordered_updates:
        middle_value = update[len(update)//2]
        score += middle_value
    return score

if __name__ == "__main__":
    print("Answer 1:", aoc1())
    print("Answer 2:", aoc2())
