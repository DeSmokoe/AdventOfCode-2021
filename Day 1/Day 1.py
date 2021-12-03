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


print(calculate_increases_solo(get_readings()))  # Puzzle 1
print(calculate_increases_windows(get_readings()))  # puzzle 2
