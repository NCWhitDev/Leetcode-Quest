def main():
  nums = [2,7,11,15] # 9
  print(twoSum(nums))
  nums = [3,2,4] # 6
  print(twoSum(nums))


def twoSum():
  # Use of target - a number to find the match
  self = {}
  for i in range(len(nums)): # only one func call
    numby = target - nums[i]
    if numby in self:       # if numby is in self
      return [self[numby], i]
    self[nums[i]] = i

if __name__ == "__main__":
    main()
