import random
import math

def binary_search(input_list: list, target: int):
    """"
    Binary search algorithm - O(log n) coplexity
    """
    counter = 0
    input_list.sort()
    start = 0
    end = len(input_list) - 1
    while True:
        middle = (end + start) // 2
        if input_list[middle] > target:
            end = middle - 1
        elif input_list[middle] < target:
            start = middle + 1
        else:
            break
        counter +=1
    print(f"Needed {counter} steps to find")


def generate_ramdom_list():
    size = math.ceil(random.random() * 10)
    return [math.ceil(random.random() * 10) for _ in range(0, size)]
    
if __name__ == "__main__":
    input_list = generate_ramdom_list()
    target = random.choice(input_list)
    print(input_list, target)
    binary_search(input_list, target)
   