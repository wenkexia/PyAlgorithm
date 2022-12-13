'''
给你一个下标从 0 开始的 m x n 二进制矩阵 grid 。

我们按照如下过程，定义一个下标从 0 开始的 m x n 差值矩阵 diff ：

令第 i 行一的数目为 onesRowi 。
令第 j 列一的数目为 onesColj 。
令第 i 行零的数目为 zerosRowi 。
令第 j 列零的数目为 zerosColj 。
diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
请你返回差值矩阵 diff 。

输入：grid = [[0,1,1],[1,0,1],[0,0,1]]
输出：[[0,0,4],[0,0,4],[-2,-2,2]]
解释：
- diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 2 + 1 - 1 - 2 = 0
- diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 2 + 1 - 1 - 2 = 0
- diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 2 + 3 - 1 - 0 = 4
- diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 2 + 1 - 1 - 2 = 0
- diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 2 + 1 - 1 - 2 = 0
- diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 2 + 3 - 1 - 0 = 4
- diff[2][0] = onesRow2 + onesCol0 - zerosRow2 - zerosCol0 = 1 + 1 - 2 - 2 = -2
- diff[2][1] = onesRow2 + onesCol1 - zerosRow2 - zerosCol1 = 1 + 1 - 2 - 2 = -2
- diff[2][2] = onesRow2 + onesCol2 - zerosRow2 - zerosCol2 = 1 + 3 - 2 - 0 = 2
'''

#优化
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        r = [0] * len(grid)
        c = [0] * len(grid[0])
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                # 行1+列1-行0-列0  遇1加1，遇0减1(优化 1)
                # 直接存储行和列的答案
                r[i] += x * 2 - 1
                c[j] += x * 2 - 1  # 1 -> 1, 0 -> -1
        for i, x in enumerate(r):
            for j, y in enumerate(c):
                # 答案可以直接填到 grid 中。
                grid[i][j] = x + y
        return grid


# grid = [[0,1,1],[1,0,1],[0,0,1]]
#直接模拟
def onesMinusZeros2(self, grid: List[List[int]]) -> List[List[int]]:

    m = len(grid)
    n = len(grid[0])
    #初始化
    row_0 = [0]*m
    row_1 = [0]*m
    col_0 = [0]*n
    col_1 = [0]*n

    diff = [[0]*n for _ in range(m)]

    for i, v in enumerate(grid):
        for j, v2 in enumerate(v):
            if v2 == 0:
                row_0[i] += 1
                col_0[j] += 1
            else:
                row_1[i] += 1
                col_1[j] += 1

    for i in range(m):
        for j in range(n):
            diff[i][j] = col_1[j]+row_1[i]-row_0[i] - col_0[j]

    return diff
