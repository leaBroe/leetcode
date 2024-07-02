

class twoSumSolution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i, num in enumerate(nums):
            if target - num in hash_map:
                return [hash_map[target - num], i]
            hash_map[num] = i
        return None

# create Solution instance
sol = twoSumSolution()
print(sol.twoSum([7,15,2,20], 9))