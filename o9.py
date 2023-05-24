class ThreeSum:
    def __init__(self, nums):
        self.nums = nums
        self.result = []
    def find_three_sum(self):
        self.result = []
        n = len(self.nums)
        self.nums.sort()

        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                current_sum = self.nums[i] + self.nums[left] + self.nums[right]
                if current_sum == 0:
                    self.result.append([self.nums[i], self.nums[left], self.nums[right]])
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        return self.result
# Example usage:
nums = [-25, -10, -7, -3, 2, 4, 8, 10]
three_sum = ThreeSum(nums)
result = three_sum.find_three_sum()
print(result)
