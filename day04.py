from utils import get_input


def add(tup1, tup2):
    return (tup1[0] + tup2[0],tup1[1] + tup2[1])

def inbounds(text, coord):
    (x,y) = coord
    return (0 <= x < len(text[0])) & (0 <= y < len(text))

def directional_search(text, coord, dir, match):
    (x,y) = coord
    next = add(coord, dir)
    if match == "":
        return True
    elif inbounds(text, next):
        if (text[next[1]][next[0]] == match[0]):
            return directional_search(text, next, dir, match[1:])
    else:
        return False

def primary_search(text, coord):
    count = 0
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            dir = (x,y)
            next = add(coord, dir)
            if inbounds(text, next):
                if (text[next[1]][next[0]] == "M"):
                    if directional_search(text, next, dir, "AS"):
                        count += 1
    return count

def primary_search_cross(text, coord):
    count = 0
    for x in [-1,1]:
        for y in [-1,1]:
            dir = (x,y)
            reverse_next = add(coord, reverse(dir))
            next = add(coord, dir)
            if inbounds(text, next) & inbounds(text, reverse_next):
                if (text[next[1]][next[0]] == "M") & (text[reverse_next[1]][reverse_next[0]] =="S"):
                    count += 1
    if count == 2:
        return 1
    else:
        return 0

def reverse(tup):
    (x,y) = tup
    return (-x,-y)

def aoc1():
    text = get_input(day=4)

    count = 0
    for y in range(len(text)):
        for x in range(len(text[0])):
            if text[y][x] == "X":
                count += primary_search(text, (x,y))

    return count

def aoc2():
    text = get_input(day=4)

    count = 0
    for y in range(len(text)):
        for x in range(len(text[0])):
            if text[y][x] == "A":
                count += primary_search_cross(text, (x,y))
    return count

if __name__ == "__main__":
    print("Answer 1:", aoc1())
    print("Answer 2:", aoc2())
