'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
'''
def main():
  nums = [3,2,3] # 3
  print(majorityElement(nums))
  nums = [2,2,1,1,1,2,2] # 2
  print(majorityElement(nums))


def majorityElement(nums):
  nums_sorted = sorted(nums)
  return nums_sorted[len(nums) // 2]

if __name__ == "__main__":
    main()
