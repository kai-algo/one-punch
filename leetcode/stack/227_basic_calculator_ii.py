"""
227. 基本计算器 II（Basic Calculator II）
难度：中等
链接：https://leetcode.cn/problems/basic-calculator-ii/

【题目】
给你一个字符串表达式 `s`，请你实现一个基本计算器来计算并返回它的值。

整数除法仅保留整数部分（向零截断）。

你可以假设给定的表达式总是有效的。所有中间结果将在 `[-2^31, 2^31 - 1]` 的范围内。

注意：不允许使用任何将字符串作为数学表达式计算的内置函数，比如 `eval()`。

【示例】
示例 1：
    输入：s = "3+2*2"
    输出：7

示例 2：
    输入：s = " 3/2 "
    输出：1

示例 3：
    输入：s = " 3+5 / 2 "
    输出：5

【约束】
- `1 <= s.length <= 3 * 10^5`
- `s` 由整数和算符 `'+'`、`'-'`、`'*'`、`'/'` 组成，中间由一些空格隔开
- `s` 表示一个有效表达式
- 表达式中的所有整数都是非负整数，且在范围 `[0, 2^31 - 1]` 内
- 题目数据保证答案是一个 32-bit 整数
"""


class Solution:
    # 这道题的核心其实在于延迟处理
    def calculate(self, s: str) -> int:
        num_stack = []
        operator_stack = []
        s = s.replace(" ", "")
        number = 0
        for w in s:
            if w.isdigit():
                number = number * 10 + int(w)
            else:
                if operator_stack:
                    last_operator = operator_stack.pop()
                    if last_operator == "+":
                        num_stack.append(number)
                    elif last_operator == "-":
                        num_stack.append(-number)
                    elif last_operator == "*":
                        right = number
                        left = num_stack.pop()
                        num_stack.append(left * right)
                    elif last_operator == "/":
                        right = number
                        left = num_stack.pop()
                        num_stack.append(int(left / right))
                else:
                    num_stack.append(number)
                operator_stack.append(w)
                number = 0
        if operator_stack:
            last_operator = operator_stack.pop()
            if last_operator == "+":
                num_stack.append(number)
            elif last_operator == "-":
                num_stack.append(-number)
            elif last_operator == "*":
                right = number
                left = num_stack.pop()
                num_stack.append(left * right)
            elif last_operator == "/":
                right = number
                left = num_stack.pop()
                num_stack.append(int(left / right))
        else:
            num_stack.append(number)

        return sum(num_stack)


"""
def calculate(self, s: str) -> int:
    s = s.replace(" ", "")
    stack = []
    sign, num = "+", 0
    for i, c in enumerate(s):
        if c.isdigit():
            num = num * 10 + int(c)
        if not c.isdigit() or i == len(s) - 1:
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))
            sign, num = c, 0
    return sum(stack)


"""
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
        ("3+2*2", 7, "示例 1：乘法优先于加法"),
        (" 3/2 ", 1, "示例 2：前后空格 + 整除"),
        (" 3+5 / 2 ", 5, "示例 3：空格夹在运算符两侧"),
        ("42", 42, "最小规模：只有一个数"),
        ("0", 0, "只有 0"),
        ("14-3/2", 13, "减法 + 除法优先"),
        ("1-1+1", 1, "连续加减从左到右"),
        ("1-2*3/4", 0, "负号与乘除混合：2*3/4=1，1-1=0"),
        ("0-7/2", -3, "除法在减号右边：7/2=3，而不是 (-7)/2 向下取整"),
        ("3-7/2*2", -3, "连续乘除从左到右：7/2=3，3*2=6，3-6=-3"),
        ("2*3*4", 24, "连续乘法"),
        ("100000000/1/2/3", 16666666, "连续除法 + 多位数"),
        ("0-2147483647", -2147483647, "边界：最大 int 与负结果"),
        ("  12  *  3 - 4  ", 32, "多位数 + 大量空格"),
    ]
    passed = 0
    for i, (*args, expected, desc) in enumerate(cases, 1):
        got = sol.calculate(*args)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
