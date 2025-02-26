from utils import get_input

from itertools import permutations

def find_frequencies(data_joined):
    frequencies = set()
    for element in data_joined:
        if element != ".":
            frequencies.add(element)
    return frequencies

class matrix:
    def __init__(self, data):
        self.data = data
        
    def __getitem__(self, key):
        x, y = key
        return self.data[y][x]
    
    def set(self, x, y, value):
        self.data[y]=self.data[y][:x]+value+self.data[y][x+1:] 

def find_index_frequency(text, frequency):
    return [i for i, ltr in enumerate(text) if ltr == frequency]

def inbounds(text, coord):
    (x,y) = coord
    return (0 <= x < len(text[0])) & (0 <= y < len(text))

def find_antinode(coord1: list, coord2: list, column_length, row_length, in_resonance = False):
    x1, y1 = coord1[0], coord1[1]
    x2, y2 = coord2[0], coord2[1]
    
    y_diff = y2-y1
    x_diff = x2-x1

    anti_node_coords = []
    if in_resonance:
        for i in range(0,max(column_length, row_length)):
            anti_node_coords.append([x2 + i * x_diff, y2 + i * y_diff])
            anti_node_coords.append([x1 - i * x_diff, y1 - i * y_diff])    
    else:
        anti_node_coords.append([x2 + x_diff, y2 + y_diff])
        anti_node_coords.append([x1 - x_diff, y1 - y_diff])    

    return anti_node_coords

def count_antinodes(data, data_joined, frequencies, in_resonance: bool) -> int:
    column_len = len(data)
    row_len = len(data[0])

    data_edit = data.copy()
    city_map_edit = matrix(data_edit)

    for frequency in list(frequencies):   # go over every frequency
        indices_long = find_index_frequency(data_joined, frequency) # find all the location (indices) with this frequency
        indices = [[index_long%len(data[0]), index_long//len(data[0])] for index_long in  indices_long] # 1D to 2D
        coordinate_combination = permutations(indices, 2)    # go over every combination of two antenna's, and calculate antinode positions
        for coordinates in coordinate_combination: 
            antinode_coords = find_antinode(coordinates[0], coordinates[1], column_len, row_len, in_resonance=in_resonance)
            for antinode_coord in antinode_coords:
                if inbounds(data_edit, tuple(antinode_coord)):
                    city_map_edit.set(antinode_coord[0], antinode_coord[1], '#')

    count = 0
    for i in range(len(data_edit[0])):
        for j in range(len(data_edit)):
            if city_map_edit[i,j] == '#':
                count += 1
    return count


def aoc1():
    data = get_input(day=8)
    data_joined = get_input(day=8, as_list=False).replace("\n", "")
    
    frequencies = find_frequencies(data_joined)

    return count_antinodes(data, data_joined, frequencies,in_resonance=False)


def aoc2():
    data = get_input(day=8)
    data_joined = get_input(day=8, as_list=False).replace("\n", "")
    
    frequencies = find_frequencies(data_joined)

    return count_antinodes(data, data_joined, frequencies, in_resonance=True)


if __name__ == "__main__":
    print("Answer 1:", aoc1())
    print("Answer 2:", aoc2())
