move = 0


def win_draw(cells):
    if cells[0] == cells[1] == cells[2]:
        return cells[0] + ' wins'
    if cells[3] == cells[4] == cells[5]:
        return cells[3] + ' wins'
    if cells[6] == cells[7] == cells[8]:
        return cells[6] + ' wins'
    if cells[0] == cells[3] == cells[6]:
        return cells[0] + ' wins'
    if cells[1] == cells[4] == cells[7]:
        return cells[1] + ' wins'
    if cells[2] == cells[5] == cells[8]:
        return cells[2] + ' wins'
    if cells[0] == cells[4] == cells[8]:
        return cells[0] + ' wins'
    if cells[2] == cells[4] == cells[6]:
        return cells[2] + ' wins'
    return 'Draw'


def enter_coordinates(cells):
    grid(cells)
    global move
    coordinates = input()
    index = 0
    coordinates = coordinates.split()
    if coordinates[0].isnumeric() and coordinates[1].isnumeric():
        coordinates[0] = int(coordinates[0])
        coordinates[1] = int(coordinates[1])
    else:
        print('You should enter numbers!')
        return enter_coordinates(cells)
    if coordinates[0] == 1 and coordinates[1] == 1:
        index = 0
    elif coordinates[0] == 1 and coordinates[1] == 2:
        index = 1
    elif coordinates[0] == 1 and coordinates[1] == 3:
        index = 2
    elif coordinates[0] == 2 and coordinates[1] == 1:
        index = 3
    elif coordinates[0] == 2 and coordinates[1] == 2:
        index = 4
    elif coordinates[0] == 2 and coordinates[1] == 3:
        index = 5
    elif coordinates[0] == 3 and coordinates[1] == 1:
        index = 6
    elif coordinates[0] == 3 and coordinates[1] == 2:
        index = 7
    elif coordinates[0] == 3 and coordinates[1] == 3:
        index = 8
    else:
        print('Coordinates should be from 1 to 3!')
        return enter_coordinates(cells)
    if cells[index] != 'X' and cells[index] != 'O' and move % 2 == 0:
        cells[index] = 'X'
        move += 1
        if move == 9 or win_draw(cells) == 'X wins':
            return grid(cells), print(win_draw(cells))
        return enter_coordinates(cells)
    elif cells[index] != 'X' and cells[index] != 'O' and move % 2 == 1:
        cells[index] = 'O'
        move += 1
        if win_draw(cells) == 'O wins':
            return grid(cells), print(win_draw(cells))
        return enter_coordinates(cells)
    else:
        print('This cell is occupied! Choose another one!')
        return enter_coordinates(cells)


def grid(cells):
    print("---------")
    for i in range(0, 8, 3):
        print(f"| {cells[i]} {cells[i + 1]} {cells[i + 2]} |")
    print("---------")


users_input = list('         ')
enter_coordinates(users_input)
