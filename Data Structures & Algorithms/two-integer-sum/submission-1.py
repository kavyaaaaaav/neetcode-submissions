class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap={}
        for i, value in enumerate(nums):
            index=target-value
            if index in prevmap:
                return [prevmap[index],i]
            prevmap[value]=i
        return
            

