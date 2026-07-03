class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        k = set(nums)
        lengthset = len(k)
        lengthlist = len(nums)
        if lengthlist == lengthset:
            return False
        else:
            return True
    
        
        

        