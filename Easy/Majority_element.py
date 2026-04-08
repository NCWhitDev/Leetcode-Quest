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

# Many ways to do this problem

# 1 way
def majorityElement(nums):
  nums_sorted = sorted(nums) # sort the array
  return nums_sorted[len(nums) // 2] # return the middle element

def sortbyCount(nums):
  sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
  return sorted_count  # [(3, 3), (2, 2), (1, 1)]

def sortbyMax(nums):
  most_common = max(count, key=lambda x: count[x])
  print(most_common)   # 3  (the key with the highest count)
  print(count[most_common])  # 3  (the count itself)
  return most_common

if __name__ == "__main__":
    main()
