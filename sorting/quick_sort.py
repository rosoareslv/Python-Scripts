# divide and coquer
# time complexity:
# best case: O(nlogn) - Geralmente quando já está ordenado -  implementar o is_sorted
# worst case O(n2) - Vai ter que percorrer o array na quantidade de seu tamanho
# space complexity:
# best case - O(logn)
# Worst case - O(n)


def quick_sort_recursive(arr, left, right):
    if left < right:
        print(arr[left : right + 1])
        pi = partition(arr, left, right)
        quick_sort_recursive(arr, left, pi - 1)
        quick_sort_recursive(arr, pi + 1, right)


def partition(arr, l, r):
    pivot = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1
