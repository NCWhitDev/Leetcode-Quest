def main():
  nums = [4,3,2,7,8,2,3,1] # [5,6]
  print(Disappeared_numbers(nums))
  nums = [1,1] # [2]
  print(Disappeared_numbers(nums))

def Disappeared_numbers(nums):
  seen=set(nums) # No dups, organized
  missing=[]
  for i in range(1, len(nums)+1): # 1 -> ... x + 1
    if i not in seen:
      missing.append(i)
  return missing
