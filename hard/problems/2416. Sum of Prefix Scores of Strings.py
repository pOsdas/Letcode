class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0


class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        root = TrieNode()

        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                node.prefix_count += 1

        ans = []
        for word in words:
            node = root
            score = 0
            for char in word:
                node = node.children[char]
                score += node.prefix_count
            ans.append(score)

        return ans
