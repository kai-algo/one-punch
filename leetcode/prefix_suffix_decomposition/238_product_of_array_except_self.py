"""
238. 除自身以外数组的乘积（Product of Array Except Self）
难度：中等
链接：https://leetcode.cn/problems/product-of-array-except-self/

【题目】
给你一个整数数组 `nums`，返回数组 `answer`，其中 `answer[i]` 等于 `nums` 中
除 `nums[i]` 之外其余各元素的乘积。

题目数据保证数组 `nums` 之中任意元素的全部前缀元素和后缀的乘积都在 32 位整数范围内。

请不要使用除法，且在 O(n) 时间复杂度内完成此题。

【示例】
示例 1：
    输入：nums = [1,2,3,4]
    输出：[24,12,8,6]

示例 2：
    输入：nums = [-1,1,0,-3,3]
    输出：[0,0,9,0,0]

【约束】
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- 输入保证数组 nums 中任意元素的全部前缀元素和后缀的乘积都在 32 位整数范围内

【进阶】
你可以在 O(1) 的额外空间复杂度内完成这个题目吗？
（出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        # 直接[1]*length就可以，元素是int，没有引用共享问题
        left = [1 for _ in range(length)]
        right = [1 for _ in range(length)]
        for i in range(1, length):
            left[i] = nums[i - 1] * left[i - 1]
        for j in range(length - 2, -1, -1):
            right[j] = nums[j + 1] * right[j + 1]
        # 循环变量作用域独立，可都用i
        return [left[k] * right[k] for k in range(length)]


# ============ 感悟 ============
# 思路：
#
# 复杂度：时间 O( )  空间 O( )
#
# 易错点 / 收获：
#
# 【Python 创建初始数组与「引用共享」】
#
# 一、一维数组：[x] * n
#   - 元素是不可变对象（int / float / str / bool / None / tuple）：放心用。
#       left = [1] * n          # 等价于 [1 for _ in range(n)]，更简洁
#     改 left[i] = 5 是「让第 i 个格子指向新对象」，不会影响别的格子。
#   - 元素是可变对象（list / dict / set）：[x] * n 复制的是「引用」，
#     n 个格子指向同一个对象，改一个全都变。
#       a = [[]] * 3
#       a[0].append(1)          # a 变成 [[1], [1], [1]]
#
# 二、二维数组：最经典的坑
#   - 错误写法：grid = [[0] * n] * m
#       外层 * m 复制的是「同一行 list 的引用」，m 行其实是同一行。
#       grid[0][0] = 1          # 每一行的第 0 列都变成 1
#   - 正确写法：grid = [[0] * n for _ in range(m)]
#       每次循环都新建一行，m 行互相独立。内层 [0] * n 没问题，因为 0 不可变。
#   - 三维同理：[[[0] * k for _ in range(n)] for _ in range(m)]
#   - 记忆口诀：最内层可以用 * ，外面每一层都要用推导式。
#
# 三、相关的拷贝问题
#   - b = a                   # 不是拷贝，只是多了一个名字，指向同一个 list
#   - b = a[:] / a.copy()     # 浅拷贝：一维数组够用；二维数组里的行仍然共享
#   - b = [row[:] for row in a]   # 二维数组的「拷贝」，LeetCode 里常用
#   - copy.deepcopy(a)        # 深拷贝，通用但较慢
#
# 四、其他相关
#   - 默认参数别用可变对象：def f(x, path=[]) 的 path 会在多次调用间共享，
#     应写成 path=None，函数内再 path = [] 。
#   - 用 id(a[0]) == id(a[1]) 可以快速验证两个格子是不是同一个对象。
#


# ============ 测试用例 ============
def run_tests():
    sol = Solution()
    cases = [
        # (nums, 期望输出, 说明)
        ([1, 2, 3, 4], [24, 12, 8, 6], "示例 1"),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0], "示例 2：含一个 0，只有 0 的位置非零"),
        ([2, 3], [3, 2], "n=2：最小规模"),
        ([1, 1, 1, 1], [1, 1, 1, 1], "全为 1"),
        ([0, 0], [0, 0], "全为 0"),
        ([0, 4], [4, 0], "n=2 且含 0"),
        ([0, 1, 2, 3], [6, 0, 0, 0], "0 在开头：只有第 0 位非零"),
        ([2, 0, 3, 0], [0, 0, 0, 0], "两个 0：全部为 0（除法做法会出错）"),
        ([-1, -2, -3], [6, 3, 2], "全负数：符号处理"),
    ]
    passed = 0
    for i, (*args, expected, desc) in enumerate(cases, 1):
        got = sol.productExceptSelf(*args)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
