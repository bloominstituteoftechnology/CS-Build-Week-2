class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # this solution swaps correctly, but not in the minimum number of steps
        # s1 = list(s1)
        # s2 = list(s2)
        # equal_buffer = moves = 0
        # while equal_buffer < len(s1):
        #     if s1[equal_buffer] != s2[equal_buffer]:
        #         try:
        #             if s2[equal_buffer] not in s2[equal_buffer + 1:]:
        #                 s1[equal_buffer], s2[equal_buffer] = s2[equal_buffer], s1[equal_buffer]
        #                 moves += 1
        #             for i in range(len(s2[equal_buffer + 1:])):
        #                 if s2[equal_buffer] == s2[equal_buffer + i + 1]:
        #                     if s1[equal_buffer + i + 1] != s2[equal_buffer + i + 1:]:
        #                         s1[equal_buffer], s2[equal_buffer + i +
        #                                              1] = s2[equal_buffer + i + 1], s1[equal_buffer]
        #                         moves += 1
        #                         break
        #         except IndexError:
        #             return -1
        #     equal_buffer += 1
        # if "".join(s1) == "".join(s2):
        #     print(s1, s2)
        #     return moves
        # else:
        #     return -1
        
        ans, sequences, visited = 0, set(), set()
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if (c1, c2) in sequences:
                    sequences.remove((c1, c2))
                    ans += 1
                else: sequences.add((c1, c2))
        for seq in sequences:
            if (seq[1], seq[0]) not in sequences: return -1
            if (seq[1], seq[0]) not in visited:
                ans += 2
                visited.add(seq)
        return ans


test = Solution()

ex1 = ["xx", "yy"]
ex2 = ["xy", "yy"]
ex3 = ["xy", "yx"]
ex4 = ["xxyyxyxyxx", "xyyxyxxxyx"]

print(test.minimumSwap(*ex1))  # 1
print(test.minimumSwap(*ex2))  # -1
print(test.minimumSwap(*ex3))  # 2
print(test.minimumSwap(*ex4))  # 4
