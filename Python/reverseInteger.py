class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31-1 or x <= -2**31:
            return 0
        
        xstr = str(abs(x))
        
        revxstr = xstr[::-1]
        
        if int(revxstr) >= 2**31-1 or int(revxstr) <= -2**31:
            return 0
        
        if x < 0:
            return int('-' + revxstr)
        
        return int(revxstr)
