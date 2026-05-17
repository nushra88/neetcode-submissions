class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        A = set(nums)
        my_dict = {}
        B = []

        for i in A:
            my_dict[i] = nums.count(i)
        
        sorted_dict = sorted(my_dict, key = my_dict.get, reverse = True)

        return sorted_dict[:k]
        
