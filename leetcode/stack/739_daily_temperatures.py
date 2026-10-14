"""
739. 每日温度（Daily Temperatures）
难度：中等
链接：https://leetcode.cn/problems/daily-temperatures/

【题目】
给定一个整数数组 `temperatures`，表示每天的温度，返回一个数组 `answer`，其中 `answer[i]` 是指对于第 `i` 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 `0` 来代替。

【示例】
示例 1：
    输入：temperatures = [73,74,75,71,69,72,76,73]
    输出：[1,1,4,2,1,1,0,0]

示例 2：
    输入：temperatures = [30,40,50,60]
    输出：[1,1,1,0]

示例 3：
    输入：temperatures = [30,60,90]
    输出：[1,1,0]

【约束】
- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        res = [0] * len(temperatures)
        # for i in range(len(temperatures)):
        # while stack:
        #     if temperatures[stack[-1]] < temperatures[i]:
        #         index = stack.pop()
        #         res[index] = i - index
        #     else:
        #         break
        # stack.append(i)
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res


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
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0], "示例 1"),
        ([30, 40, 50, 60], [1, 1, 1, 0], "示例 2：严格递增"),
        ([30, 60, 90], [1, 1, 0], "示例 3"),
        ([50], [0], "最小规模：只有一天"),
        ([80, 70, 60, 50], [0, 0, 0, 0], "严格递减：栈一直不弹"),
        ([60, 60, 60], [0, 0, 0], "全相同：相等不算更高"),
        ([70, 60, 70, 80], [3, 1, 1, 0], "相等温度夹在中间：弹栈用 < 而不是 <="),
    ]
    passed = 0
    for i, (*args, expected, desc) in enumerate(cases, 1):
        got = sol.dailyTemperatures(*args)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
