"""
208. 实现 Trie (前缀树)（Implement Trie (Prefix Tree)）
难度：中等
链接：https://leetcode.cn/problems/implement-trie-prefix-tree/

【题目】
Trie（发音类似 "try"）或者说前缀树是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。
这一数据结构有相当多的应用情景，例如自动补全和拼写检查。

请你实现 Trie 类：
- `Trie()` 初始化前缀树对象。
- `void insert(String word)` 向前缀树中插入字符串 `word`。
- `boolean search(String word)` 如果字符串 `word` 在前缀树中，返回 `true`（即，在检索之前已经插入）；
  否则，返回 `false`。
- `boolean startsWith(String prefix)` 如果之前已经插入的字符串 `word` 的前缀之一为 `prefix`，
  返回 `true`；否则，返回 `false`。

【示例】
示例 1：
    输入：
        ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
        [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    输出：
        [null, null, true, false, true, null, true]
    解释：
        Trie trie = new Trie();
        trie.insert("apple");
        trie.search("apple");   // 返回 True
        trie.search("app");     // 返回 False
        trie.startsWith("app"); // 返回 True
        trie.insert("app");
        trie.search("app");     // 返回 True

【约束】
- `1 <= word.length, prefix.length <= 2000`
- `word` 和 `prefix` 仅由小写英文字母组成
- `insert`、`search` 和 `startsWith` 调用次数 总计 不超过 `3 * 10^4` 次
"""


class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.childrens:
                cur.childrens[w] = TrieNode()
            cur = cur.childrens[w]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w in cur.childrens:
                cur = cur.childrens[w]
            else:
                return False
        if cur.is_end:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if w in cur.childrens:
                cur = cur.childrens[w]
            else:
                return False
        return True


# ============ 感悟 ============
# 思路：
#
# 复杂度：时间 O( )  空间 O( )
#
# 易错点 / 收获：
#


# ============ 测试用例 ============
def run_tests():
    # 每个用例是一串操作 [(方法名, 参数, 期望返回值), ...]，insert 的期望为 None
    cases = [
        (
            [
                ("insert", "apple", None),
                ("search", "apple", True),
                ("search", "app", False),
                ("startsWith", "app", True),
                ("insert", "app", None),
                ("search", "app", True),
            ],
            "示例 1",
        ),
        (
            [
                ("search", "a", False),
                ("startsWith", "a", False),
            ],
            "空 Trie：查询都应为 False",
        ),
        (
            [
                ("insert", "a", None),
                ("search", "a", True),
                ("startsWith", "a", True),
                ("search", "b", False),
            ],
            "单字符",
        ),
        (
            [
                ("insert", "apple", None),
                ("search", "apples", False),
                ("startsWith", "apples", False),
                ("startsWith", "apple", True),
            ],
            "查询词比已有词更长：不能越界，且整词也是自己的前缀",
        ),
        (
            [
                ("insert", "app", None),
                ("insert", "apple", None),
                ("insert", "apply", None),
                ("search", "appl", False),
                ("startsWith", "appl", True),
                ("search", "apple", True),
                ("search", "apply", True),
            ],
            "共享前缀：appl 只是前缀，不是单词（需要结束标记）",
        ),
        (
            [
                ("insert", "abc", None),
                ("insert", "abc", None),
                ("search", "abc", True),
                ("search", "ab", False),
            ],
            "重复插入",
        ),
    ]
    passed = 0
    for i, (ops, desc) in enumerate(cases, 1):
        trie = Trie()
        ok = True
        detail = ""
        for method, arg, expected in ops:
            got = getattr(trie, method)(arg)
            if got != expected:
                ok = False
                detail = f"：{method}({arg!r}) 期望 {expected}, 实际 {got}"
                break
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}{detail}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
