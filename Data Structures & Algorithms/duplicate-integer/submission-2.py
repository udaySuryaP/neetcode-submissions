class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag=False
        
        length=len(nums)
        setLength=len(set(nums))
        if(length!=setLength):
            flag=True
        
        return flag
