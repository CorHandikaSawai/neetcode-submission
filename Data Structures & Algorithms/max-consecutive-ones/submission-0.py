class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp = 0
        counter = 0
        for num in nums:
            if num == 1:
                temp += 1
                if temp >= counter:
                    counter = temp
            else:
                temp = 0
        
        return counter
                
