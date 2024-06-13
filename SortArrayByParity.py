class Solution:
    def sortArrayByParity(self, nums):

        if not nums:
            return nums
        
        evens = []
        odds = []

        for i in nums:
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)

        return evens + odds