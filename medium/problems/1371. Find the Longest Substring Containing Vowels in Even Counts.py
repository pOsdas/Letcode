def findTheLongestSubstring(s: str) -> int:
    def all_vowels_even(count) -> bool:
        return all(count % 2 == 0 for count in count.values())

    vowels = 'aeiou'

    vowel_count = {v: 0 for v in vowels}
    max_length = 0

    for start in range(len(s)):
        for v in vowels:
            vowel_count[v] = 0

        for end in range(start, len(s)):
            if s[end] in vowel_count:
                vowel_count[s[end]] += 1

            if all_vowels_even(vowel_count):
                max_length = max(max_length, end - start + 1)

    return max_length


