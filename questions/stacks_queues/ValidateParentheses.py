"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.

Input: "()"     Input: "()[]{}"  Input: "(]"     Input: "([)]"   Input: "{[]}"
Output: true    Output: true     Output: false   Output: false   Output: true

Ref: https://leetcode.com/problems/valid-parentheses/solution/

@author a.k
"""
from questions.recursion_dp.Parens import sol
from data_structures.Stack import Stack

closed_parens = [')', ']', '}']
matching_open_paren = {')': '(', ']': '[', '}': '{'}


def valid_parenthesis(s: str) -> bool:
    """
    Returns whether the parenthetical expression, s, is valid.
    @Algorithm: - Keep track of open parens that require terminating using a stack
                - If we encounter an open paren, push to indicate we are still to find a terminating closed paren
                - If we encounter a closed paren,
                    - If open paren stack is empty, then we cannot match the closed paren to anything -- invalid
                    - Check if closed paren terminates the open paren at the top of the stack
                        - If it does, pop() the open paren to indicate we have found its termination
                        - If it doesn't, then -- invalid
    :param s: string with parentheses
    :Time: O(N)
    :Space: O(N)
    :return: true if valid
    """
    open_parens = Stack()  # tracks history of open parentheses that need to be terminated
    for c in s:
        if c in closed_parens:  # if closed paren, check if top of stack is open paren of same type
            if open_parens.get_size() == 0:
                return False  # no open paren to match this closed paren

            if open_parens.peek() == matching_open_paren[c]:  # proper termination found for open paren at top of stack
                open_parens.pop()  # pop to indicate this paren has found a terminating closing paren
            else:
                return False  # incorrect termination
        else:
            open_parens.push(c)  # if open paren, add to stack

    return open_parens.is_empty()  # if stack is empty, valid; else, indicates an open paren hasn't been terminated


if __name__ == '__main__':
    tests = ['()', '()[]{}', '(]', ')', ')(', '([)]', '{[]}', '())']
    ans = [True, True, False, False, False, False, True, False]
    for t, a, in zip(tests, ans):
        assert valid_parenthesis(t) == a, 'ERROR!!'

    tests = sol(4) + sol(2) + sol(2)
    for t in tests:
        assert valid_parenthesis(t), 'ERROR!!'

    print('PASSED!')
