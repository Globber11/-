from itertools import permutations
from time import time

array = [1, 2, 3, 4, 5, 6]

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


def johnson_trotter(n):
    permutation = list(range(1, n + 1))
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
print('Алгортим Нараяны:')
tic = time()
print(narayana(array))
toc = time() - tic
print('Время работы:', toc)

print('Алгортим Джонсона-Троттера:')
tic = time()
n = 6
for perm in johnson_trotter(n):
    print(perm)
toc = time() - tic
print('Время работы:', toc)

print('Встроеннный алгортим библиотеки itertools:')
tic = time()
permutations = permutations(array)
for perm in permutations:
    print(perm)
toc = time() - tic
print('Время работы:', toc)