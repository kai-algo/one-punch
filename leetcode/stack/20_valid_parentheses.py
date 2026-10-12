"""
20. 有效的括号（Valid Parentheses）
难度：简单
链接：https://leetcode.cn/problems/valid-parentheses/

【题目】
给定一个只包括 `'('`，`')'`，`'{'`，`'}'`，`'['`，`']'` 的字符串 `s`，判断字符串是否有效。

有效字符串需满足：
1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。
3. 每个右括号都有一个对应的相同类型的左括号。

【示例】
示例 1：
    输入：s = "()"
    输出：true

示例 2：
    输入：s = "()[]{}"
    输出：true

示例 3：
    输入：s = "(]"
    输出：false

示例 4：
    输入：s = "([])"
    输出：true

示例 5：
    输入：s = "([)]"
    输出：false

【约束】
- `1 <= s.length <= 10^4`
- `s` 仅由括号 `'()[]{}'` 组成
"""


class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {")": "(", "]": "[", "}": "{"}
        stack = []
        for w in s:
            if w not in parentheses_map:
                stack.append(w)
            else:
                if not stack:
                    return False
                elif stack.pop() != parentheses_map[w]:
                    return False
        # 在这里写解答
        return not stack


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
        ("()", True, "示例 1"),
        ("()[]{}", True, "示例 2：多组并列"),
        ("(]", False, "示例 3：类型不匹配"),
        ("([])", True, "示例 4：嵌套"),
        ("([)]", False, "示例 5：交叉，顺序错误"),
        ("(", False, "最小规模：只有左括号，结束时栈非空"),
        (")", False, "最小规模：只有右括号，栈为空时不能 pop"),
        ("((", False, "全是左括号"),
        ("{[]}", True, "三层嵌套"),
        ("(){}}{", False, "前半有效，后面多出右括号"),
    ]
    passed = 0
    for i, (*args, expected, desc) in enumerate(cases, 1):
        got = sol.isValid(*args)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
