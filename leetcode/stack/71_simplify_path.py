"""
71. 简化路径（Simplify Path）
难度：中等
链接：https://leetcode.cn/problems/simplify-path/

【题目】
给你一个字符串 `path`，表示指向某一文件或目录的 Unix 风格绝对路径（以 `'/'` 开头），请你将其转化为更加简洁的规范路径。

在 Unix 风格的文件系统中规则如下：
- 一个点 `'.'` 表示当前目录本身。
- 两个点 `'..'` 表示将目录切换到上一级（指向父目录）。
- 任意多个连续的斜杠（即 `'//'` 或 `'///'`）都被视为单个斜杠 `'/'`。
- 任何其他格式的点（例如 `'...'` 或 `'....'`）均被视为有效的文件/目录名称。

返回的简化路径必须遵循下述格式：
- 始终以斜杠 `'/'` 开头。
- 两个目录名之间必须只有一个斜杠 `'/'`。
- 最后一个目录名（如果存在）不能以 `'/'` 结尾。
- 此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即不含 `'.'` 或 `'..'`）。

返回简化后得到的规范路径。

【示例】
示例 1：
    输入：path = "/home/"
    输出："/home"
    解释：注意，最后一个目录名后面没有斜杠。

示例 2：
    输入：path = "/home//foo/"
    输出："/home/foo"
    解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。

示例 3：
    输入：path = "/home/user/Documents/../Pictures"
    输出："/home/user/Pictures"
    解释：两个点 `..` 表示上一级目录（父目录）。

示例 4：
    输入：path = "/../"
    输出："/"
    解释：不可能从根目录上升一级目录。

示例 5：
    输入：path = "/.../a/../b/c/../d/./"
    输出："/.../b/d"
    解释："..." 在这个问题中是一个合法的目录名。

【约束】
- `1 <= path.length <= 3000`
- `path` 由英文字母、数字、`'.'`、`'/'` 或 `'_'` 组成
- `path` 是一个有效的 Unix 风格绝对路径
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        stack = []
        for p in path_list:
            if p == "." or p == "":
                continue
            elif p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)


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
        ("/home/", "/home", "示例 1：末尾斜杠去掉"),
        ("/home//foo/", "/home/foo", "示例 2：连续斜杠合并"),
        (
            "/home/user/Documents/../Pictures",
            "/home/user/Pictures",
            "示例 3：.. 回退一级",
        ),
        ("/../", "/", "示例 4：根目录不能再上升"),
        ("/.../a/../b/c/../d/./", "/.../b/d", "示例 5：... 是合法目录名"),
        ("/", "/", "最小规模：只有根目录"),
        ("/a/./b/../../c/", "/c", ". 忽略 + 连续回退"),
        ("/a/../../b", "/b", "回退越过根目录后继续"),
        ("/..hidden/.x/..", "/..hidden", "以点开头但不是 . / .. 的合法名称"),
        ("/a/b/c/../../..", "/", "全部回退到根，结果必须是 '/' 而非空串"),
    ]
    passed = 0
    for i, (*args, expected, desc) in enumerate(cases, 1):
        got = sol.simplifyPath(*args)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
