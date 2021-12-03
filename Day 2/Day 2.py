import numpy as np

def get_instructions():
    with open('Puzzle Input.txt') as f:
        lines = f.read().splitlines()
        f.close()
        return lines


def split_instructions(dirty_instructions):
    numbers = np.array([])
    instructions = np.array([])
    for instruction in range(len(dirty_instructions)):
        for part in dirty_instructions[instruction].split():
            if part.isdigit():
                numbers = np.append(numbers, part)
            else:
                instructions = np.append(instructions, part)
    instructions = np.stack((instructions, numbers), axis=1)
    return instructions


def calculate_destination(instructions):  # Puzzle 1 route instructions
    position = [0, 0]

    for i in range(len(instructions)):
        if instructions[i, 0] == 'forward':
            position[0] = position[0] + int(instructions[i, 1])
        elif instructions[i, 0] == 'down':
            position[1] = position[1] + int(instructions[i, 1])
        else:
            position[1] = position[1] - int(instructions[i, 1])
    return position


def calculate_destination_aim(instructions):  # Puzzle 2 route instructions
    position = [0, 0]
    aim = 0

    for i in range(len(instructions)):
        if instructions[i, 0] == 'forward':
            position[0] = position[0] + int(instructions[i, 1])
            position[1] = position[1] + int(instructions[i, 1])*aim
        elif instructions[i, 0] == 'down':
            aim = aim + int(instructions[i, 1])
        else:
            aim = aim - int(instructions[i, 1])
    return position


print(calculate_destination(split_instructions(get_instructions())))  # Puzzle 1
print(calculate_destination_aim(split_instructions(get_instructions())))  # Puzzle 2

