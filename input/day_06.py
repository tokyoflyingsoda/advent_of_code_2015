import re

with open('day_06.txt', 'r') as file_object:
    input_text = file_object.read()

def count_lit_lights(instructions):
    grid = [[0] * 1000 for _ in range(1000)]
    pattern = re.compile(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)')
    for line in instructions.strip().split('\n'):
        match = pattern.search(line)
        if not match:
            continue
        action = match.group(1)
        x1, y1 = int(match.group(2)), int(match.group(3))
        x2, y2 = int(match.group(4)), int(match.group(5))
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if action == 'turn on':
                    grid[y][x] += 1
                elif action == 'turn off' and grid[y][x]>0:
                    grid[y][x] -= 1
                elif action == 'toggle':
                    grid[y][x] += 2
    total_lit = sum(sum(row) for row in grid)
    return total_lit
print(count_lit_lights(input_text))