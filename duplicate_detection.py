from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_num = set(nums)
        if len(new_num)!= len(nums):
            return True
        return False
        
       