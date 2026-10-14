"""
503. 下一个更大元素 II（Next Greater Element II）
难度：中等
链接：https://leetcode.cn/problems/next-greater-element-ii/

【题目】
给定一个循环数组 `nums`（`nums[nums.length - 1]` 的下一个元素是 `nums[0]`），返回 `nums` 中每个元素的**下一个更大元素**。

数字 `x` 的**下一个更大的元素**是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 `-1`。

【示例】
示例 1：
    输入：nums = [1,2,1]
    输出：[2,-1,2]
    解释：第一个 1 的下一个更大的数是 2；
        数字 2 找不到下一个更大的数；
        第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

示例 2：
    输入：nums = [1,2,3,4,3]
    输出：[2,3,4,-1,4]

【约束】
- `1 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
"""


class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
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
        # (输入参数..., 期望输出, 说明)
        ([1, 2, 1], [2, -1, 2], "示例 1：靠循环找到答案"),
        ([1, 2, 3, 4, 3], [2, 3, 4, -1, 4], "示例 2"),
        ([5], [-1], "最小规模：单元素"),
        ([5, 5, 5], [-1, -1, -1], "全相同：没有严格更大的数"),
        ([3, 2, 1], [-1, 3, 3], "递减：后面的元素都要靠循环回到开头"),
        ([-1, -2, -3], [-1, -1, -1], "全负数 + 递减：最大值本身为 -1"),
        ([2, 1, 2, 4, 3], [4, 2, 4, -1, 4], "最大值在中间，最后一个元素靠循环"),
    ]
    passed = 0
    for i, (*args, expected, desc) in enumerate(cases, 1):
        got = sol.nextGreaterElements(*args)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
