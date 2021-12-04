import numpy as np

def get_diagnostics():
    with open('Puzzle_Input.txt') as f:
        lines = f.read().splitlines()
        f.close()
        return list(lines)

def split_binaries(diagnostics):
    lst = diagnostics.copy()
    for binary in diagnostics:
        lst[diagnostics.index(binary)] = [int(char) for char in binary]
    return np.array(lst)

def get_ones_zeros(split_diagnostics):
    ones = list(range(len(split_diagnostics[0])))
    for i in ones:
        ones[i] = sum(split_diagnostics[:, i])
    zeros = list(1000 - np.array(ones.copy()))
    return ones, zeros

def get_gamma_epsilon(ones, zeros):
    most, least = list(range(len(ones))), list(range(len(ones)))
    for i in range(len(ones)):
        if ones[i] > zeros[i]:
            most[i] = '1'
            least[i] = '0'
        else:
            most[i] = '0'
            least[i] = '1'
    gamma = int(''.join(most), 2)
    epsilon = int(''.join(least), 2)
    power = gamma*epsilon
    return gamma, epsilon, power


print(get_gamma_epsilon(get_ones_zeros(split_binaries(get_diagnostics()))[0], get_ones_zeros(split_binaries(get_diagnostics()))[1]))


