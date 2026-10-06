# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
def findDisappearedNumbers(self, nums):
        seen=set(nums) # No dups, organized
        missing=[]
        for i in range(1, len(nums)+1): # 1 -> ... + 1
            if i not in seen:
                missing.append(i)
        return missing
