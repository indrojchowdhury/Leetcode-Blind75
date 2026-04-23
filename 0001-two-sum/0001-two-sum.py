class Solution:
    def twoSum(self,nums:list[int],target=int)->list[int]:
        num_map={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in num_map:
                return [num_map[diff],i]
            num_map[num]=i