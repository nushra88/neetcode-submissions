class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    pass
                elif(nums[i]+nums[j]==target):
                    if(i>j):
                        return [j,i]
                    return [i,j]