"""
Implement a method to perform basic string compression using counts of repeated characters (@see RLE)
E.g. s = "aabcccccaaa" -> "a2b1c5a3"

if the compressed string is larger, return original

N.B. python implementation will be slower because we don't have a "StringBuilder"

@author a.k
"""


def compress(s: str) -> str:
    """
    Compresses the string using repeated character counts.
    @Algorithm: - for each character, if current character is not equal to the next or if we reached the end
                - append the current character as well as the count we have set
    :param s: string to be compressed
    :Time: O(n + k^2) n = length and k = number of character sequences
    :Space: O(n)
    :return: compressed string or original if original length is smaller
    """
    compressed = ""
    consecutive = 0
    for i in range(len(s)):
        consecutive += 1
        if i >= len(s) - 1 or s[i] != s[i + 1]:
            compressed += s[i] + str(consecutive)
            consecutive = 0
    return compressed if len(compressed) < len(s) else s


if __name__ == '__main__':
    tests = ["aabcccccaaa", "aaaa", "aaab", "a", "cba", "abbbbbbbbbba"]
    ans = ["a2b1c5a3", "a4", "aaab", "a", "cba", "a1b10a1"]
    for t, a in zip(tests, ans):
        assert a == compress(t), "Error!"
    print('PASSED')
