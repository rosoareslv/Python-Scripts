import random
import math


# Complexidade
# Temporal - O(log N)
# Espacial - O(1)
# A lista precisa estar ordenada
def binary_search(arr: list, target: int, start = 0, end = None):
    """ "
    Binary search algorithm - O(log n) coplexity
    """
    steps = 0
    if end == None:
        end = len(arr) - 1
    while start <= end:
        steps += 1
        index = (end + start) // 2
        if arr[index] == target:
            print(f"Needed {steps} steps to find!")
            return index
        if arr[index] > target:
            end = index - 1
        else:
            start = index + 1
    return -1


# Mesma complexidade da binary search e utiliza esse algoritmo em sua busca, serve para arrays muito grande
#vai dobrando o index para achar o target, ou passar do valor para gerar uma substring, com o start do index /2 e o final index
#para ser jogado no algoritmo da binary search
def exponential_search(arr: list, target: int):
    if arr[0] == target:
        return 0
    i = 1
    while i < len(arr) and arr[i] < target:
        i *= 2
    if arr[i] == target:
        return i
    return binary_search(arr, target, i//2, i if i < (len(arr) -1) else len(arr) -1)

def generate_ramdom_list():
    size = math.ceil(random.random() * 10)
    return [math.ceil(random.random() * 10) for _ in range(0, size)]


if __name__ == "__main__":
    input_list = generate_ramdom_list()
    target = random.choice(input_list)
    # print(input_list, target)
    # x = binary_search(input_list, target)

    x = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        37,
        38,
        39,
        40,
    ]
    
    r = exponential_search(x, 32)
    
    print(r)
