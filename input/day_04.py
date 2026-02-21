with open('day_04.txt', 'r') as file_object:
    input_text = file_object.read()

def count_lucky_houses_with_robo(instructions):
    santa_x, santa_y = 0, 0
    robo_x, robo_y = 0, 0

    visited_houses = {(0, 0)}

    for index, move in enumerate(instructions):
        dx, dy = 0, 0
        if move == '^':
            dy = 1
        elif move == 'v':
            dy = -1
        elif move == '>':
            dx = 1
        elif move == '<':
            dx = -1

        if index % 2 == 0:
            santa_x += dx
            santa_y += dy
            visited_houses.add((santa_x, santa_y))
        else:
            robo_x += dx
            robo_y += dy
            visited_houses.add((robo_x, robo_y))

    return len(visited_houses)

print(count_lucky_houses_with_robo(input_text))