def main():
  nums = [3,0,1] # 2
  print(missingnumber(nums))
  nums = [0,1] # 2
  print(missingnumber(nums))

def missingnumber(nums):
  missing = []
  for i in range(0, len(nums)+1):
     if i not in nums:
        return i

if __name__ == "__main__":
    main()
