from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_length = len(words[0])
        total_length = word_length * len(words)
        words_count = Counter(words)

        output = []

        for i in range(len(s) - total_length + 1):
            current_words = [s[j:j+word_length] for j in range(i, i + total_length, word_length)]
            if Counter(current_words) == words_count:
                output.append(i)

        return output


# s = Solution()
# print(s.findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]))

