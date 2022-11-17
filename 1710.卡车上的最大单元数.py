'''
Author: Arts 1184664659@qq.com
FilePath: 1710.卡车上的最大单元数.py
Date: 2022-11-15 22:38:47
LastEditors: Arts 1184664659@qq.com
LastEditTime: 2022-11-16 20:39:26
Description:
'''
#
# @lc app=leetcode.cn id=1710 lang=python
#
# [1710] 卡车上的最大单元数
#

# @lc code=start

class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        # boxTypes = [[1,3],[2,2],[3,1]]
        n=len(boxTypes)
        boxTypes.sort(key =lambda x:x[1],reverse =True)
        ans= 0
        for numberOfBoxes,numberOfUnits in boxTypes:
            if truckSize >= numberOfBoxes:
                ans += numberOfBoxes * numberOfUnits
                truckSize -= numberOfBoxes
            else:
                ans += truckSize * numberOfUnits
                break
        return ans


# @lc code=end
if __name__ == "__main__":
    # s = Solution()
    # print(s.maximumUnits())
    boxTypes = [[1,3],[2,2],[3,1]]
    for numberOfBoxes, numberOfUnitsPerBox in boxTypes:
        print(numberOfBoxes, numberOfUnitsPerBox)