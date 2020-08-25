class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        prefix = ""
        try:
            base = strs[0]  # test case is the first element
            for i in range(len(base)):
                for item in strs[1:]:  # cut off the first one, it's redundant to check
                    if item[i] != base[i]:
                        return prefix  # returns earl whenever a non-match is found
                prefix += base[i]
        except IndexError:
            pass
        return prefix 

def print_prefix(s):
    print(f"prefix: \"{s}\"")

test = Solution()

x1 = ["flower", "flow", "flight"]
x2 = ["dog", "racecar", "car"]

print_prefix(test.longestCommonPrefix(x1))  # should return "fl"
print_prefix(test.longestCommonPrefix(x2))  # should return ""
