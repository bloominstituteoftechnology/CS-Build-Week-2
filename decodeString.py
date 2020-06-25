"""
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
"""

class Solution:
    def decodeString(self, s: str) -> str:
        iteration_count = "" # treat nums as strings to avoid dealing w/ bases/positions
        counts = [] # "stack" to store iteration counts
        chars = [] # "stack" to store alphabetical chars
        string = "" # output
        
        for char in s:
            
            if char.isdigit():
                iteration_count += char
            
            elif char == "[":
                # iteration count always comes before "[", push to stack
                counts.append((int(iteration_count)))
                # push preceeding string to chars stack
                chars.append(string)
                # reset string and iteration_count for next set of letters
                string = ""
                iteration_count = ""
            
            elif char == "]":
                # done w/ a "unit of work", so pop everything off the stacks and multiply
                string = chars.pop() + (counts.pop() * string)
            
            else: # must be alpha 
                string += char
                
        return string
            
