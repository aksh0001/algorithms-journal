"""
Given a roman numeral, convert it back to an integer.
Input: "III" Output: 3
Input: "IV" Output: 4
Input: "IX" Output: 9
Input: "LVIII" Output: 58; Explanation: L = 50, V= 5, III = 3.
Input: "MCMXCIV" Output: 1994; Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

@author a.k
"""
map_symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_to_int(s: str) -> int:
    """
    Converts s into an integer.
    @Algorithm: - Simply map and add each char to a running total
                - Only interesting case happens when the next char is of greater value;
                    - this indicates we should map and subtract the next value with our current before adding to total.
    :param s: string of roman.
    :Time: O(N)
    :Space: O(1)
    :return: integer representation.
    """
    ret_val, i = 0, 0
    while i < len(s):
        if i + 1 < len(s) and greater(s[i + 1], s[i]):  # if next is greater subtract with current
            ret_val, i = ret_val + map_symbol[s[i + 1]] - map_symbol[s[i]], i + 2
        else:
            ret_val, i = ret_val + map_symbol[s[i]], i + 1
    return ret_val


def greater(r1, r2) -> bool:
    """
    Returns true if roman 1 is greater than roman 2.
    """
    return map_symbol[r1] > map_symbol[r2]


if __name__ == '__main__':
    tests = ['III', 'IV', 'IX', 'LVIII', 'MCMXCIV']
    ans = [3, 4, 9, 58, 1994]
    for t, a in zip(tests, ans):
        assert roman_to_int(t) == a, 'ERROR!'
    print('PASSED')
