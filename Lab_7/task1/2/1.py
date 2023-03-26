class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

# runtime: 5401 ms 
# memory : 14.9 MB 



class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        seen = dict()

        for i, n in enumerate(nums):
            if (target - n) in seen.keys():
                return ([seen[target - n], i])
            
            seen[n] = i
            
# runtime: 62 ms
# memory : 15.1 MB