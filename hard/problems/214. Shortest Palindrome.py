def shortestPalindrome(s: str) -> str:
    if not s or s == s[::-1]:
        return s

    rev_s = s[::-1]
    new_s = s + "#" + rev_s
    n = len(new_s)
    lps = [0] * n

    for i in range(1, n):
        length = lps[i - 1]
        while length > 0 and new_s[i] != new_s[length]:
            length = lps[length - 1]
        if new_s[i] == new_s[length]:
            length += 1
        lps[i] = length

    palindrome_len = lps[-1]
    return rev_s[:len(s) - palindrome_len] + s
