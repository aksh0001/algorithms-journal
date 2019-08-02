"""
Count all possible decodings of a digit sequence.
Let 'a' map to 1, 'b' -> 2, 'c' -> 3,..., 'z' -> 26.

e.g. Input:  digits[] = "121"
Output: 3
// The possible decodings are "ABA", "AU", "LA"

Input: digits[] = "1234"
Output: 3
// The possible decodings are "ABCD", "LCD", "AWD"

Ref: https://www.youtube.com/watch?v=qli-JCrSwuk
EXTENSION: Return the possible decodings
"""
import time


def naive(s: str) -> int:
    def aux(s: str, n: int) -> int:
        """
        Returns the total number of ways to decode a string of length n according to the char mappings
        :param s: string
        :param n: length of string
        :Time: O(2^N) (e.g. f(6) calls f(5) and f(4) and so on... - like fibonacci)
        :Space: O(N) stack space
        :return: total ways to decode the string
        """
        if s[n - 1] == '0':  # If character we are looking at is a 0, there are no ways to decode it
            return 0
        if n == 0 or n == 1:  # If empty string or a single character, then only one way to decode
            return 1
        result = aux(s, n - 1)  # First rec call to recur on n - 1, since s[n] is always decodable
        if n >= 2 and 10 <= int(s[n - 2] + s[n - 1]) <= 26:
            result += aux(s, n - 2)  # Second rec call to recur on n - 2, only if the two chars we're looking at <= 26
        return result

    return aux(s, len(s))


def num_ways(s: str) -> int:
    def aux(s: str, n: int, memo: list) -> int:
        """
        Returns the total number of ways to decode a string of length n according to the char mappings
        :param s: string
        :param n: length of string
        :param memo: memo[n] = total ways to decode the string, s[0..n]
        :Time: O(N)
        :Space: O(N) stack space
        :return: total ways to decode the string
        """
        if memo[n] is not None:  # If we have already computed the value, return it
            return memo[n]
        if s[n - 1] == '0':
            return 0
        if n == 0 or n == 1:
            return 1
        result = aux(s, n - 1, memo)
        if n >= 2 and 10 <= int(s[n - 2] + s[n - 1]) <= 26:
            result += aux(s, n - 2, memo)
        memo[n] = result
        return result

    memo = [None] * (len(s) + 1)
    return aux(s, len(s), memo)


if __name__ == "__main__":
    print("Testing...")
    tests = ['3', '1234', '121', '2735', '27315', '011', "111111111111111111111111111111"]
    ans = [1, 3, 3, 1, 2, 0, 1346269]
    t1 = time.time()
    for t, a in zip(tests, ans):
        if a is not None:
            assert naive(t) == a, "Error! {} {}".format(t, a)
    t2 = time.time()
    print("NAIVE PASSED, time =", t2 - t1)
    t3 = time.time()
    for t, a in zip(tests, ans):
        if a is not None:
            assert num_ways(t) == a, "Error! {} {}".format(t, a)
    t4 = time.time()
    print("DP PASSED, time =", t3 - t4)
    print(">>>ALL PASSED<<<")
