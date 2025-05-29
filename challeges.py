
#https://leetcode.com/problems/two-sum/description/
def twoSum(nums, target):
    obj = {}
    for i, num in enumerate(nums):
        rest = target - num
        if obj.get(rest):
            return obj[rest], i
        obj[num] = i


if __name__ ==  "__main__":
    twoSum([])