from itertools import permutations
from time import time

array = [1352, 2345, 3345, 46, 5345345, 66]

def time_decorator(func):
    def wrapper(araay):
        tic = time()
        print(func(array))
        toc = time() - tic
        print('Время работы:', toc)
    return wrapper

@time_decorator
def narayana(list):
    def backtrack(start):
            if start == len(list):
                result.append(list.copy())
                return
            used = set()
            for i in range(start, len(list)):
                if list[i] in used:
                    continue
                used.add(list[i])
                list[start], list[i] = list[i], list[start]
                backtrack(start + 1)
                list[start], list[i] = list[i], list[start]
    result = []
    backtrack(0)
    return result

@time_decorator
def johnson_trotter(list_):
    n = len(list_)
    permutation = list_
    directions = [-1] * n
    result = [permutation.copy()]
    while True:
        mobile_index = -1
        mobile_element = -1
        for i in range(n):
            direction = directions[i]
            if (i + direction >= 0 and i + direction < n and
                permutation[i] > permutation[i + direction] and
                permutation[i] > mobile_element):
                mobile_element = permutation[i]
                mobile_index = i

        if mobile_index == -1:
            break
        direction = directions[mobile_index]
        swap_index = mobile_index + direction
        permutation[mobile_index], permutation[swap_index] = permutation[swap_index], permutation[mobile_index]
        directions[mobile_index], directions[swap_index] = directions[swap_index], directions[mobile_index]

        for i in range(n):
            if permutation[i] > mobile_element:
                directions[i] = -directions[i]

        result.append(permutation.copy())
    return result

if __name__ == '__main__':
    narayana(array)
    johnson_trotter(array)
    tic = time()
    permutations = permutations(array)
    for perm in permutations:
        print(perm)
    toc = time() - tic
    print('Время работы:', toc)
