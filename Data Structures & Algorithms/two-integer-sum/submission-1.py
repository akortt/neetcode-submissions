class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute-Force Approach
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # HashMap Approach
        hashmap = {}
        for index, number in enumerate(nums):
            difference = target - number
            if difference in hashmap:
                return [hashmap[difference], index]
            hashmap[number] = index
                