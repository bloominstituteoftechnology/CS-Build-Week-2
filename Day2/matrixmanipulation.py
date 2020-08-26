class Solution():
    def mutateMatrix(self, a, q):
        midpoint = (len(a) - 1) / 2

        def clockwise(coords):
            i, j = coords
            di = i - midpoint
            dj = j - midpoint

            ni = midpoint - dj
            nj = midpoint - di
            # print(f"di: {di} - dj: {dj}")

            # print(f"{i}, {j} -> {ni}, {nj}")
            return (int(ni), int(nj))

        def reflectmain(coords):
            # top-left to bottom-right diagonal
            i, j = coords
            di = i - midpoint
            dj = j - midpoint
            ni = midpoint + dj
            nj = midpoint + di
            # print(f"{i}, {j} -> {ni}, {nj}")
            return (int(ni), int(nj))

        def reflectsecond(coords):
            # top-right to bottom-left diagonal
            i, j = coords
            di = i - midpoint
            dj = j - midpoint
            ni = midpoint - dj
            nj = midpoint - di
            # print(f"{i}, {j} -> {ni}, {nj}")
            return (int(ni), int(nj))

        maptable = {}
        for i in range(len(a)):
            for j in range(len(a)):
                if (i, j) not in maptable:
                    maptable[(i, j)] = {
                        0: None,
                        1: reflectmain((i, j)),
                        2: reflectsecond((i, j))
                    }
                # clockwise((i, j))
                # print(f"({i}, {j}) -> {a[i][j]}")

        print(maptable)
        funcmap = {
            0: clockwise,
            1: reflectmain,
            2: reflectsecond
        }
        # print(maptable)

        return a


test = Solution()

ex1 = [[
    [1, 2],
    [3, 4]
], [0, 1, 2]]

ex2 = [[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], [0, 1, 2]]

# print(test.mutateMatrix(*ex1))
print(test.mutateMatrix(*ex2))
