# time complexity:
# best case: O(n) - Geralmente quando já está ordenado -  implementar o is_sorted
# worst case O(n2) - Vai ter que percorrer o array na quantidade de seu tamanho
# space complexity - 0(1) - nao existe alocação de array


def bubble_sort(nums):
    size = len(nums)
    for _ in nums:
        is_sorted = True
        print(nums)
        for i in range(size - 1):
            if nums[i] > nums[i + 1]:
                is_sorted = False
                nums[i + 1], nums[i] = nums[i], nums[i + 1]
        if is_sorted:
            break
    return nums
