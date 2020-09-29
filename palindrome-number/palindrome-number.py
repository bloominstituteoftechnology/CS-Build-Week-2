class Solution:
    def isPalindrome(self, x: int) -> bool:
        # quickly check if x is negative b/c neg ints can't be palindromes
        if x < 0:
            # if negative, return false
            return False
        # quickly check if x is a single digit, it will always be a palindrome
        if x < 10:
            # if it is, return true
            return True
        # initialize count to be 0
        count = 0
        # initialize empty list
        lst = []
        # loop through the input 
        while x > 0:
            count += 1
            # take mod of input and append to empty list
            lst.append(x % 10)
            # double divide the input by 10 to check if the append num is correct
            x = x // 10
            
        for i in range (count // 2):
            if lst[i] == lst[count -i - 1]:
                continue
                
            else:                
                return False
        
        return True