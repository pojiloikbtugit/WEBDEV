def max_end3(nums):
  res = []
  for num in nums:
    max_val = max(nums[0], nums[len(nums) - 1])
    res.append(max_val)
    res.append(max_val)
    res.append(max_val)
    return res
 
    