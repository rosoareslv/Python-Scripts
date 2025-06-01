
#https://leetcode.com/problems/two-sum/description/
def two_sum(nums, target):
    obj = {}
    for i, num in enumerate(nums):
        rest = target - num
        if obj.get(rest):
            return obj[rest], i
        obj[num] = i

#https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
# Envolve conceito de two pointer
def reverse_words_manual(word):
    res = ''
    l, r = 0,0 
    while r < len(word):
        if word[r] != ' ':
            r += 1
        else:
            res += word[l:r][::-1] + ' '
            r += 1
            l = r
    res += word[l:r][::-1]
    return res

#Sliding Window -> while dentro de while
#https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/description/
def maximum_length_substring(s):
    l, r = 0, 1
    max = 0
    characters = {}
    characters[s[l]] = 1
    while r < len(s):
        if characters.get(s[r]):
            characters[s[r]] += 1
        else:
            characters[s[r]] = 1
        while characters[s[r]] == 3:
            characters[s[l]] -= 1
            l += 1
        max = r - l + 1 if r - l + 1 > max else max
        r += 1
    return max

#https://leetcode.com/problems/first-unique-character-in-a-string/description/
def first_uniq_char(s):
    characters = {}
    index = 0
    for char in s:
        if characters.get(char) is None:
            characters[char] = [index, 1]
        else:
            characters[char][1] += 1
        index +=1
    for char, data in characters.items():
        if data[1] == 1:
            return data[0]
    return -1

#http://leetcode.com/problems/contains-duplicate-ii/description/
def contains_nearby_duplicate(nums,  k):
    values = {}
    i = 0
    while i < len(nums):
        if values.get(nums[i]) is None:
            values[nums[i]] = i
        elif abs(values.get(nums[i]) - i) <= k: 
            return True
        else:
            values[nums[i]] = i
        i +=1
    return False

#https://leetcode.com/problems/length-of-last-word/
def length_of_last_word(s):
    i = len(s) - 1
    count = 0
    while i < len(s):
        if s[i] != ' ':
            count += 1
        elif count > 0:
            return count
        if i > 0:
            i -= 1
        else:
            return count
        
#https://leetcode.com/problems/power-of-two/
def is_power_of_two(n):
    if n <= 0:
        return False
    elif n == 1:
        return True
    while n >= 2:
        if n % 2 == 0:
            n = n / 2
        else: 
            return False
    return True
    
        
        
    
if __name__ ==  "__main__":
    #print(contains_nearby_duplicate([1,2,3,1,2,3], 2))
    print(length_of_last_word("luffy is still joyboy"))
    print(is_power_of_two(40))