def centered_average(nums):
  nums = sorted(nums)
  nums.remove(nums[0])
  nums.remove(nums[-1])
  return(sum(nums)/len(nums))
