def get_readings():
    with open('Day 1/DepthMeters.txt') as f:
        lines = f.read().splitlines()
        f.close()
        return lines


def calculate_increases_solo(input_list):
    counter = 0

    for s in range(len(input_list)-1):
        if int(input_list[s+1]) > int(input_list[s]):
            counter = counter + 1
    return counter

def calculate_increases_windows(input_list):
    counter = 0

    for s in range(len(input_list)-1):
        try:
            if int(input_list[s+1]) + int(input_list[s+2]) + int(input_list[s+3]) >\
                    int(input_list[s]) + int(input_list[s+1]) + int(input_list[s+2]):
                counter = counter + 1
        except IndexError:
            pass
    return counter


lst = get_readings()
Depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

print(calculate_increases_solo(lst))  # Puzzle 1
print(calculate_increases_windows(lst))  # puzzle 2
