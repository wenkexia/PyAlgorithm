#
# @lc app=leetcode.cn id=2383 lang=python
#
# [2383] 赢得比赛需要的最少训练时长
'''
击败条件：需要在经验和精力上都 严格 超过对手才能击败他们
击败第 i 个对手会使你的经验 增加 experience[i]，但会将你的精力 减少  energy[i] 。

每训练一个小时，你可以选择将增加经验增加 1 或者 将精力增加 1 。

可以分开考虑在比赛开始前，需要最少增加的精力和经验数量。
每次遇到一个对手，当前精力值都需要严格大于当前对手，否则需要增加精力值。因此，在击败最后一个对手后，剩余的精力值至少要为 1。记所有对手的精力和为 sm，比赛开始前需要达到的最少精力即为 sm+1 ，否则需要进行sm+1−initialEnergy 小时的训练。

'''



#

# @lc code=start
class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        """
        :type initialEnergy: int 初始精力
        :type initialExperience: int 初始经验
        :type energy: List[int]
        :type experience: List[int]
        :rtype: int
        """
        sm = sum(energy)
        trainingHours = 0 if initialEnergy > sm else sm + 1 - initialEnergy
        for e in experience:
            if initialExperience <= e:
                trainingHours += 1 + (e - initialExperience)
                initialExperience = 2 * e + 1
            else:
                initialExperience += e
        return trainingHours


# @lc code=end


initialEnergy = 5
initialExperience = 3
energy = [1,4,3,2]
experience = [2,6,3,1]
s = Solution()
s.minNumberOfHours(initialEnergy, initialExperience, energy, experience)