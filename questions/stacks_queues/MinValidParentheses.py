"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')',
and in any positions ) so that the resulting parentheses string is valid.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

Input: "())"
Output: 1

Input: "((("
Output: 3

Input: "()"
Output: 0

Input: "()))(("
Output: 4

Approach: the "same-ol'" stack-based validation approach! (90% Time on the first attempt!)
N.B. can be done even more straightforward by simply counting! O(1) space

@author a.k
"""


def minAddToMakeValid(s: str) -> int:
    """
    Returns the minimum number of parens (open or closed) to add to make s a valid parentheses expression.
    @Algorithm:
    # If see an open paren, push onto stack to indicate we still need to find the matching closed paren
    # If see a closed paren, pop open paren off stack to indicate its matching brace found
    # If unexpectedly see a closed paren with empty stack (an invalid exp), incr counter by 1 to indicate we need to add 1 open to make valid
    # If there are remaining open parens remaining in the stack after parsing, add those to indicate there weren't any matching closed parens
    # therefore min_to_add = len(stack) after parsing + running count of "wild" closed parens
    # Easy!
    :param s: parentheses expression
    :Time: O(N)
    :Space: O(N)
    :return: minimum number of parens to add t make valid
    """
    open_parens, wild_closed_paren_cnt = [], 0
    for c in s:
        if c == ')' and len(open_parens) == 0:  # found a wild closed paren!
            wild_closed_paren_cnt += 1
        elif c == '(':  # push open paren onto stack
            open_parens.append('(')
        elif c == ')':  # found a corresponding closed paren for an open paren, pop it!
            open_parens.pop()
    return len(open_parens) + wild_closed_paren_cnt


if __name__ == '__main__':
    test = "()))(("
    assert minAddToMakeValid(test) == 4
    print('PASSED')
