from typing import List
from collections import defaultdict, deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        global b

        def cluster(x, y):  # 聚类
            grid_1[x].append(y)
            grid[x][y] = 0
            for j in pro:
                x1, y1 = x + j[0], y + j[1]
                if 0 <= x1 < le_x and 0 <= y1 < le_y:
                    if grid[x1][y1] == 1:
                        cluster(x1, y1)

        def diffuse(x, y, level):  # 单点扩散
            #pro移动的方向
            for k in pro:
                x1, y1 = x + k[0], y + k[1]
                if 0 <= x1 < le_x and 0 <= y1 < le_y:
                    if grid[x1][y1] == 0:
                        if y1 in grid_1[x1]:
                            return True
                        grid[x1][y1] = level
                        b[x1].append(y1)
            return False

        grid_1 = defaultdict(list)
        grid_2 = defaultdict(list)
        pro = {(1, 0), (0, 1), (0, -1), (-1, 0)}
        le_x = len(grid)
        le_y = len(grid[0])
        tf = True
        for index_i, i in enumerate(grid):  # 全体遍历
            for index_j, j in enumerate(i):
                if tf and j == 1:  # 遇到1直接开始聚类，只是执行一次
                    cluster(index_i, index_j)
                    tf = False
                elif j == 1:  # 记录聚类之后剩下的那个岛的坐标
                    grid_2[index_i].append(index_j)
        level = 1

        while 1:  # 关于剩下的第二个岛的扩散
            b = defaultdict(list)
            for i in list(grid_2.keys()):

                for j in grid_2[i]:  # 逐个遍历逐个扩散
                    tf = diffuse(i, j, level + 1)
                    if tf: break
                if tf: break
            if tf: break
            level += 1
            grid_2 = b
        return level - 1


S = Solution()
# print(S.shortestBridge([[0, 1, 0, 0, 0],
#                         [0, 1, 0, 1, 1],
#                         [0, 0, 0, 0, 1],
#                         [0, 0, 0, 0, 0],
#                         [0, 0, 0, 0, 0]]))
print(S.shortestBridge([[1, 1, 1, 1, 1],
                        [1, 0, 0, 0, 1],
                        [1, 0, 1, 0, 1],
                        [1, 0, 0, 0, 1],
                        [1, 1, 1, 1, 1]]))
# [[0, 0, 3, 0, 0],
#  [0, 3, 2, 3, 0],
#  [3, 2, 1, 2, 3],
#  [0, 3, 2, 3, 0],
#  [0, 0, 3, 0, 0]]
# print(S.shortestBridge([[1, 1, 1, 1, 1],
#                         [1, 0, 0, 0, 1],
#                         [0, 0, 0, 0, 0],
#                         [0, 0, 0, 0, 0],
#                         [0, 0, 1, 0, 0]]))
"""----------------------------------聚类----------------------------------------------"""
# a = collections.defaultdict(list)
# pro = {(1, 0), (0, 1), (0, -1), (-1, 0)}
# #        下      右       左        上
# grid = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
# le_x = len(grid)
# le_y = len(grid[0])
#
#
# def cluster(x, y):
#     a[x].append(y)
#     grid[x][y] = 0
#     for j in pro:
#         if 0 <= x + j[0] < le_x and 0 <= y + j[1] < le_y:
#             if grid[x + j[0]][y + j[1]] == 1 and y + j[1] not in a[x + j[0]]:
#                 cluster(x + j[0], y + j[1])
#     return
#
#
# cluster(0, 0)
# print(a)
# print(grid)
"""------------------------------官方-----------------------------------------------"""
"""
方法一：广度优先搜索
题目中求最少的翻转 0 的数目等价于求矩阵中两个岛的最短距离，因此我们可以广度优先搜索来找到矩阵中两个块的最短距离。
首先找到其中一座岛，然后将其不断向外延伸一圈，直到到达了另一座岛，延伸的圈数即为最短距离。
广度优先搜索时，我们可以将已经遍历过的位置标记为 -1，实际计算过程如下：
我们通过遍历找到数组 grid 中的 1 后进行广度优先搜索，此时可以得到第一座岛的位置集合，记为island，并将其位置全部标记为 -1。
随后我们从 island 中的所有位置开始进行广度优先搜索，当它们到达了任意的 1 时，即表示搜索到了第二个岛，搜索的层数就是答案。
"""
"""
方法二：深度优先搜索 + 广度优先搜索
解法思路与方法一类似，我们可以利用深度优先搜索求出其中的一座岛，
然后利用广度优先搜索来找到两座岛的最短距离。深度度优先搜索时，我们可以将已经遍历过的位置标记为 −1，实际计算过程如下：
我们通过遍历找到数组 grid 中的 1 后进行深度优先搜索，此时可以得到第一座岛的位置集合，记为island，并将其位置全部标记为 −1。
随后我们从 island 中的所有位置开始进行广度优先搜索，当它们到达了任意的 1 时，即表示搜索到了第二个岛，搜索的层数就是答案。

"""


class Solution2:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v != 1:
                    continue
                island = []
                grid[i][j] = -1
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    island.append((x, y))
                    for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                            grid[nx][ny] = -1
                            q.append((nx, ny))

                step = 0
                q = island
                while True:
                    tmp = q
                    q = []
                    for x, y in tmp:
                        for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                            if 0 <= nx < n and 0 <= ny < n:
                                if grid[nx][ny] == 1:
                                    return step
                                if grid[nx][ny] == 0:
                                    grid[nx][ny] = -1
                                    q.append((nx, ny))
                    step += 1

    def shortestBridge2(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v != 1:
                    continue
                q = []

                def dfs(x: int, y: int) -> None:
                    grid[x][y] = -1
                    q.append((x, y))
                    for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                            dfs(nx, ny)

                dfs(i, j)

                step = 0
                while True:
                    tmp = q
                    q = []
                    for x, y in tmp:
                        for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                            if 0 <= nx < n and 0 <= ny < n:
                                if grid[nx][ny] == 1:
                                    return step
                                if grid[nx][ny] == 0:
                                    grid[nx][ny] = -1
                                    q.append((nx, ny))
                    step += 1


S = Solution2()
print(S.shortestBridge2([[0, 1, 0, 0, 0],
                         [0, 1, 0, 1, 1],
                         [0, 0, 0, 0, 1],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0]]))
