"""
42. 接雨水（Trapping Rain Water）
难度：困难
链接：https://leetcode.cn/problems/trapping-rain-water/

【题目】
给定 `n` 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，
下雨之后能接多少雨水。

【示例】
示例 1：
    输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
    输出：6
    解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，
         在这种情况下，可以接 6 个单位的雨水。

示例 2：
    输入：height = [4,2,0,3,2,5]
    输出：9

【约束】
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 在这里写解答
        pass


# ============ 感悟 ============
# 思路：
#
# 复杂度：时间 O( )  空间 O( )
#
# 易错点 / 收获：
#


# ============ 测试用例 ============
def run_tests():
    sol = Solution()
    cases = [
        # (height, 期望输出, 说明)
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6, "示例 1"),
        ([4, 2, 0, 3, 2, 5], 9, "示例 2"),
        ([5], 0, "n=1：最小规模"),
        ([0, 0, 0], 0, "全为 0"),
        ([3, 3, 3], 0, "全相同：无凹槽"),
        ([1, 2, 3, 4, 5], 0, "严格递增：右边没有挡板"),
        ([5, 4, 3, 2, 1], 0, "严格递减：左边没有挡板"),
        ([2, 0, 2], 2, "最简单的凹槽"),
        ([4, 2, 3], 1, "水位由较矮的一侧决定：min(4,3)-2"),
        ([3, 0, 0, 2, 0, 4], 10, "多个槽，水位取两侧最大值的较小者：3+3+1+3"),
        ([5, 2, 1, 2, 1, 5], 14, "两边高中间低：3+4+3+4"),
    ]
    passed = 0
    for i, (*args, expected, desc) in enumerate(cases, 1):
        got = sol.trap(*args)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
