with open('day_02.txt', 'r') as file_object:
    input_text = file_object.read()

floor = 0

for index, char in enumerate(input_text):
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1
    if floor == -1:
        position = index + 1
        print(position)
        break