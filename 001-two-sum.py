class Solution:
    def __init__(self):
        self.num_to_index = {}

    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            complement = target - num
            if complement in self.num_to_index:
                return [self.num_to_index[complement], i]
            self.num_to_index[num] = i

        return None

# Example usage:
nums = [2, 7, 11, 15]
target = 9   

result = Solution().twoSum(nums, target)
print(result)  # Output: [0, 1]
