"""
84. 柱状图中最大的矩形（Largest Rectangle in Histogram）
难度：困难
链接：https://leetcode.cn/problems/largest-rectangle-in-histogram/

【题目】
给定 `n` 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 `1`。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

【示例】
示例 1：
    输入：heights = [2,1,5,6,2,3]
    输出：10
    解释：最大的矩形为图中红色区域（高度 5、6 的两根柱子），面积为 10。

示例 2：
    输入：heights = [2,4]
    输出：4

【约束】
- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`
"""


class Solution:
    # 其实不用左右都搞，只需要从左往右就可以，来回两遍相当于重复计算了！
    # def largestRectangleArea(self, heights: list[int]) -> int:
    #     stack = []
    #     res = 0
    #     for i, h in enumerate([0] + heights + [0]):   # 两端补 0 做哨兵
    #         while stack and stack[-1][1] > h:
    #             _, top_h = stack.pop()
    #             left = stack[-1][0]
    #             res = max(res, top_h * (i - left - 1))
    #         stack.append((i, h))
    #     return res
    def largestRectangleArea(self, heights: list[int]) -> int:
        len_h = len(heights)
        left_stack = []
        left_ans = [0] * len_h
        for i, h in enumerate(heights):
            while left_stack and heights[left_stack[-1]] > h:
                index = left_stack.pop()
                left_ans[index] = i - index - 1
            left_stack.append(i)
        while left_stack and heights[left_stack[-1]] > 0:
            index = left_stack.pop()
            left_ans[index] = len_h - index - 1

        # print(left_ans)
        right_stack = []
        right_ans = [0] * len_h
        for i in range(len_h - 1, -1, -1):
            while right_stack and heights[right_stack[-1]] > heights[i]:
                index = right_stack.pop()
                right_ans[index] = index - i - 1
            right_stack.append(i)
        while right_stack and heights[right_stack[-1]] > 0:
            index = right_stack.pop()
            right_ans[index] = index
        # print(right_ans)
        max_rect = 0
        for i, h in enumerate(heights):
            max_rect = max(max_rect, h * (left_ans[i] + right_ans[i] + 1))

        return max_rect


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
        # (输入参数..., 期望输出, 说明)
        ([2, 1, 5, 6, 2, 3], 10, "示例 1"),
        ([2, 4], 4, "示例 2"),
        ([5], 5, "最小规模：单根柱子"),
        ([0], 0, "只有高度 0"),
        ([2, 2, 2], 6, "全相同：矩形横跨全部"),
        ([1, 2, 3, 4, 5], 9, "严格递增：遍历结束后栈里还有元素，需要清算"),
        ([5, 4, 3, 2, 1], 9, "严格递减：每个元素都会弹出前一个"),
        ([2, 1, 2], 3, "中间矮、两边高：最矮的柱子能横跨全部"),
        ([0, 9], 9, "含 0：0 把左边隔断"),
        ([6, 2, 5, 4, 5, 1, 6], 12, "经典用例：2 5 4 5 横跨 4 格高度 3"),
    ]
    passed = 0
    for i, (*args, expected, desc) in enumerate(cases, 1):
        got = sol.largestRectangleArea(*args)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
