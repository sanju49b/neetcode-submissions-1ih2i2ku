class Solution:
    def isPalindrome(self, s: str) -> bool:
        # the two pointer approach
        x = ''.join(char.lower() for char in s if char.isalnum())
        left,right = 0,len(x)-1
        while left <= right:
            if x[left] != x[right]:
                return False
                break
            else:
                left += 1
                right -= 1
        return True