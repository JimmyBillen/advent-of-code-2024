from utils import get_input

class matrix:
    def __init__(self, data):
        self.data = data
        
    def __getitem__(self, key):
        x, y = key
        return self.data[y][x]
    
    def set(self, x, y, value):
        self.data[y]=self.data[y][:x]+value+self.data[y][x+1:]

def matrixForm(row, column, data):
    return data[column][row]

def change_90degr(dir):
    if dir == (-1,0):
        return 0, -1
    if dir == (0, -1):
        return 1,0
    if dir == (1,0):
        return 0,1
    if dir == (0,1):
        return -1,0
    return (dir[0]+1)%3-1, (dir[1]+1)%3-1

def add(tup1, tup2):
    return (tup1[0] + tup2[0],tup1[1] + tup2[1])

def inbounds(text, coord):
    (x,y) = coord
    return (0 <= x < len(text[0])) & (0 <= y < len(text))


def aoc1(return_visited_coords=False):
    puzzle_str = get_input(day=6, as_list=False)
    puzzle_one_line = puzzle_str.replace("\n", "")
    index_start = puzzle_one_line.index('^') 

    puzzle = get_input(day=6)

    column_len = len(puzzle) # 130
    row_len = len(puzzle[0]) # 130

    column_start = index_start // row_len 
    row_start = index_start % row_len

    matrix_data = matrix(puzzle)

    dir = (0,-1) # left/right, up/down (since start = ^)
    coord = row_start, column_start
    new_coord = coord

    visited_coords = set()
    while inbounds(puzzle, new_coord):
        if matrix_data[new_coord[0], new_coord[1]] == '#': # if blocked, change direction
            dir = change_90degr(dir)
        else: # move forward
            coord = new_coord
            matrix_data.set(coord[0], coord[1], 'X')
            visited_coords.add(coord)
        new_coord = add(coord, dir)

    if return_visited_coords:
        return visited_coords

    return len(visited_coords)


def aoc2():
    puzzle_str = get_input(day=6, as_list=False)
    puzzle_one_line = puzzle_str.replace("\n", "")
    index_start = puzzle_one_line.index('^') 

    puzzle = get_input(day=6)

    column_len = len(puzzle) # 130
    row_len = len(puzzle[0]) # 130

    column_start = index_start // row_len    # column start index
    row_start = index_start % row_len    # row start index       

    visited_coords_list = aoc1(return_visited_coords=True)
    count = 0
    coordsWhereBlocked = []
    for index, visited_coord in enumerate(visited_coords_list):
        print("progress:", index/len(visited_coords_list), end='\r')
        x, y = visited_coord[0], visited_coord[1]
        
        data = puzzle.copy()
        matrix_data = matrix(data)

        if x == row_start and y == column_start:
            continue
        else:
            matrix_data.set(x, y,'#')

        dir = (0,-1) # left/right, up/down (since start = ^)

        coord = row_start, column_start
        new_coord = add(coord, dir)

        while inbounds(data, new_coord):
            if matrix_data[new_coord[0], new_coord[1]] == '#':
                dir = change_90degr(dir)
            else:
                current_val_str = matrix_data[coord[0], coord[1]]
                if current_val_str.isdigit():
                    if int(current_val_str) > 4: # if a tile was visited more than 4 times -> stuck in loop
                        count += 1
                        coordsWhereBlocked.append((x,y))
                        break
                    else: # visited tile again, +1 to visit count of that tile
                        new_val_str = str(int(current_val_str) + 1)
                        matrix_data.set(coord[0], coord[1], new_val_str)
                else: # if never visited before
                    matrix_data.set(coord[0], coord[1], '1')
                coord = new_coord
            new_coord = add(coord, dir)
    print("\n")
    return count

if __name__ == "__main__":
    print("Answer 1:", aoc1())
    print("Answer 2:", aoc2())
