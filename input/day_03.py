with open('day_03.txt', 'r') as file_object:
    input_text = file_object.read()

def count_lucky_houses(instructions):
    x, y = 0, 0
    visited_houses = {(x, y)}

    for move in instructions:
        if move == '^':
            y += 1
        elif move == 'v':
            y -= 1
        elif move == '>':
            x += 1
        elif move == '<':
            x -= 1

        visited_houses.add((x, y))

    return len(visited_houses)


print(f"visits: {count_lucky_houses(input_text)}")
