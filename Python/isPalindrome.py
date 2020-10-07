class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        xList = list(map(int, str(x)))
        xReverse = xList[::-1]
        
        return xList == xReverse
