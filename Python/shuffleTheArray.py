class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        xnums = nums[:len(nums)//2]
        ynums = nums[len(nums)//2:]
        shuffled = []
        
        for i in range(n):
            shuffled.append(xnums[i])
            shuffled.append(ynums[i])
            
        return shuffled
