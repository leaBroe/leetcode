
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def two_sum(nums, target):
    storage = {}
    for i in range(len(nums)):

        current_number = nums[i]
        complement = target - current_number

        if storage.get(complement) != None:
            return [i, storage[complement]]

        storage[current_number] = i
        print(storage)

    return None


#solution = two_sum([2,7,11,15], 9)

solution = two_sum([3, 2, 4], 6)

#solution = two_sum([3, 3], 6)


print(solution)