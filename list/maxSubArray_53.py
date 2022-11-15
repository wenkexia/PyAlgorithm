'''
53. 最大子数组和

给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组 是数组中的一个连续部分。
'''


'''
动态规划
f(i) 代表以第 i个数结尾的「连续子数组的最大和」
状态方程：f(i)=max{f(i−1)+nums[i],nums[i]}
'''
def maxSubArray(nums) -> int:
    current = 0
    ans = nums[0]
    for i in range(len(nums)):
        current = max(current+nums[i],nums[i])
        ans = max(ans,current)
    return ans


def maxSubArray1(nums) -> int:
    for index,x in enumerate(nums[1:],1):
        




if __name__ =='__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))
