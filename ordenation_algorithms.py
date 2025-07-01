
#time complexity:
#best case: O(n) - Geralmente quando já está ordenado -  implementar o is_sorted
#worst case O(n2) - Vai ter que percorrer o array na quantidade de seu tamanho
#space complexity - 0(1) - nao existe alocação de array

def bubble_sort(nums):
    size = len(nums)
    for _ in nums:
        is_sorted = True
        print(nums)
        for i in range(size -1):
            if nums[i] > nums[i+1]:
                is_sorted = False
                nums[i+1], nums[i] = nums[i], nums[i+1]
        if is_sorted:
            break
    return nums

#divide and coquer
#time complexity:
#best case: O(nlogn) - Geralmente quando já está ordenado -  implementar o is_sorted
#worst case O(n2) - Vai ter que percorrer o array na quantidade de seu tamanho
#space complexity:
#best case - O(logn)
#Worst case - O(n)

def quick_sort_recursive(arr, left, right):
    if left < right:
        print(arr[left:right+1])
        pi = partition(arr, left, right)
        quick_sort_recursive(arr, left, pi-1)
        quick_sort_recursive(arr, pi + 1, right)
    

def partition(arr, l, r):
    pivot = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= pivot:   
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1
            

if __name__ == "__main__":
    quick_sort_recursive(arr, 0, len(arr) - 1)

    #bubble_sort([5,4,3,2,1])
    bubble_sort([1,2,4,5,3])
                

