from collections import Counter
import numpy as np


def get_diagnostics(filename):
    with open(filename) as f:
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


def get_oxygen_co2(split_diagnostics):
    oxygen = list(range(len(split_diagnostics[0])))
    co2 = list(range(len(split_diagnostics[0])))
    smaller_list1 = split_diagnostics.copy()
    smaller_list2 = split_diagnostics.copy()
    for i in range(len(oxygen)):
        data1 = Counter(smaller_list1[:, i]).most_common(2)[0][1]
        if data1 == 1 or data1 == smaller_list1.shape[0]/2:
            most_common = 1
        else:
            most_common = Counter(smaller_list1[:, i]).most_common(2)[0][0]
        try:
            data2 = Counter(smaller_list2[:, i]).most_common(2)[1][1]
            if data2 == 1 or data2 == smaller_list2.shape[0]/2:
                least_common = 0
            else:
                least_common = Counter(smaller_list2[:, i]).most_common(2)[1][0]
        except IndexError:
            least_common = 0
        element1 = 0
        element2 = 0
        while element1 < smaller_list1.shape[0] != 1:
            if smaller_list1[element1, i] == most_common:
                element1 = element1 + 1
            else:
                smaller_list1 = np.delete(smaller_list1, element1, axis=0)
        while element2 < smaller_list2.shape[0] != 1:
            if smaller_list2[element2, i] == least_common:
                element2 = element2+1
            else:
                smaller_list2 = np.delete(smaller_list2, element2, axis=0)
    strings1 = [str(integer) for integer in smaller_list1[0]]
    oxygen = int("".join(strings1), 2)
    strings2 = [str(integer) for integer in smaller_list2[0]]
    co2 = int("".join(strings2), 2)
    return oxygen, co2, oxygen*co2



#  print(get_gamma_epsilon(get_ones_zeros(split_binaries(get_diagnostics()))[0], get_ones_zeros(split_binaries(get_diagnostics()))[1]))
print(get_oxygen_co2(split_binaries(get_diagnostics('Puzzle_Input.txt'))))
#  print(get_oxygen_co2(split_binaries(get_diagnostics('Test input.txt'))))

