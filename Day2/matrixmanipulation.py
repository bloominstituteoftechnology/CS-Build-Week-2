class Solution():
    def mutateMatrix(self, a, q):
        midpoint = (len(a) - 1) / 2

        def rotate90Clockwise(A):
            # code needs to be adapted
            N = len(A[0]) 
            for i in range(N // 2): 
                for j in range(i, N - i - 1): 
                    temp = A[i][j] 
                    A[i][j] = A[N - 1 - j][i] 
                    A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j] 
                    A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i] 
                    A[j][N - 1 - i] = temp
        def clockwise(coords):
            i, j = coords
            di = abs(i - midpoint)
            dj = abs(j - midpoint)
            if di < 0 and dj < 0:
                ni = i
                nj = dj + midpoint
            elif di < 0 and dj > 0:
                ni = midpoint + di
                nj = j
            elif di > 0 and dj > 0:
                ni = i
                nj = midpoint - dj
            elif di < 0 and dj > 0:
                ni = midpoint - di
                nj = j
            else:
                pass

            print(f"{i}, {j} -> {int(ni)}, {int(nj)}")
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
                        0: clockwise((i, j)),
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
