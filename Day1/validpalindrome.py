class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        iterate over the string from the front while checking the back simultaneously
        keep track of the left and right indices you're checking
        if you ever find a mismatch, return False
        when right < left, return True
        to handle non-alphnum chars, add two while loops at the start of the outer loop,
            one for the left that increments left while not s[left].isalnum()
            one for the right that decrements right while not s[right].isalnum()
        
        initialize the string to lowercase
        """
        if len(s) <= 1:
            return True
        left = 0
        right = len(s) - 1
        while right >= left:
            try:
                while not s[left].isalnum():
                    left += 1
                while not s[right].isalnum():
                    right -= 1
            except IndexError:
                return True
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

test = Solution()

ex1 = "A man, a plan, a canal, Panama!"
ex2 = "Abba"
ex3 = "This one isn't"

print(test.isPalindrome(ex1))
print(test.isPalindrome(ex2))
print(test.isPalindrome(ex3))