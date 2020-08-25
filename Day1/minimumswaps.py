class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        #         i1 = {"x": [], "y": []}
        #         i2 = {"x": [], "y": []}

        #         for i in range(len(s1)):
        #             i1[s1[i]].append(i)

        #         for i in range(len(s2)):
        #             i2[s2[i]].append(i)

        #         if (len(i1["x"]) + len(i2["x"])) % 2 != 0 or (len(i1["y"]) + len(i2["y"])) % 2 != 0:
        #             return -1
        s1 = list(s1)
        s2 = list(s2)
        equal_buffer = moves = 0
        while equal_buffer < len(s1):
            if s1[equal_buffer] != s2[equal_buffer]:
                try:
                    if s2[equal_buffer] not in s2[equal_buffer + 1:]:
                        s1[equal_buffer], s2[equal_buffer] = s2[equal_buffer], s1[equal_buffer]
                        moves += 1
                    for i in range(len(s2[equal_buffer + 1:])):
                        if s2[equal_buffer] == s2[equal_buffer + i + 1]:
                            if s1[equal_buffer + i + 1] != s2[equal_buffer + i + 1:]:
                                s1[equal_buffer], s2[equal_buffer + i +
                                                     1] = s2[equal_buffer + i + 1], s1[equal_buffer]
                                moves += 1
                                break
                except IndexError:
                    return -1
            equal_buffer += 1
        if "".join(s1) == "".join(s2):
            print(s1, s2)
            return moves
        else:
            return -1


test = Solution()

ex1 = ["xx", "yy"]
ex2 = ["xy", "yy"]
ex3 = ["xy", "yx"]
ex4 = ["xxyyxyxyxx", "xyyxyxxxyx"]

print(test.minimumSwap(*ex1))  # 1
print(test.minimumSwap(*ex2))  # -1
print(test.minimumSwap(*ex3))  # 2
print(test.minimumSwap(*ex4))  # 4
