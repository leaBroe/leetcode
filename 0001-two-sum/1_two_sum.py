
def get_solution(nums, target):
    hm = {} # hm is an empty dictionary that will store the numbers as keys and their indices as values.

    for i in range(len(nums)):
        num = nums[i] # store the current number
        print(num)
        cmp = target - num # cmp calculates the complement of the current number (num) which is needed to reach the target (i.e., target - num)
        print(cmp)

        if (hm.get(cmp) != None): # checks if cmp exists in the dictionary hm. If it does, it means that the current number and the complement of the current number add up to the target.
            print(hm)
            return [i, hm[cmp]]

        hm[num] = i

    return hm


solution = get_solution([2,7,11,15], 9)
print(solution)

