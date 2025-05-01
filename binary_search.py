

#divide to conquer
def main():
    counter = 0
    target = 3
    input_list = [1,2,4,3]
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


if __name__ == "__main__":
    main()
