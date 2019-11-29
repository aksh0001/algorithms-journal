"""
todo!
"""


class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip()
        opn_stack = []
        opt_stack = []
        result = 0
        # Iterate through each character
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                # Loop through until you finish parsing the digit
                c = extract_number(s, i)
                opn_stack.append(c)
            elif is_operator(c):
                # while top of stack has a higher precedence than current operator
                # evaluate it
                top = peek_stack(opt_stack)
                while opt_stack and has_higher_precedence(top, c):
                    top = opt_stack.pop()
                    op1 = opn_stack.pop()
                    op2 = opn_stack.pop()
                    temp = eval_subexpression(op2, op1, top)
                    result = temp
                    opn_stack.append(temp)

                opt_stack.append(c)

        while len(opt_stack) != 0:
            top = opt_stack.pop()
            op1 = opn_stack.pop()
            op2 = opn_stack.pop()
            temp = eval_subexpression(op2, op1, top)
            result = temp
            opn_stack.append(temp)

        return result


def peek_stack(stack):
    if stack:
        return stack[-1]


def is_operator(c: chr):
    if c == '+' or c == '-' or c == '*' or c == '/':
        return True
    else:
        return False


def eval_subexpression(op1, op2, operator):
    op1 = int(op1)
    op2 = int(op2)
    if operator == '+':
        return op1 + op2
    elif operator == '-':
        return op1 - op2
    elif operator == '*':
        return op1 * op2
    elif operator == '/':
        return op1 // op2
    else:
        raise Exception('Error!')


def has_higher_precedence(operator1, operator2):
    if operator1 == '/':
        return True
    if operator2 == '/':
        return False
    if operator1 == '*':
        return True
    if operator2 == '+' or operator2 == '-':
        return True
    return False


def extract_number(s: str, i: int):
    num = ''
    while i < len(s) and s[i].isdigit():
        num += s[i]
        i += 1
    return num


if __name__ == '__main__':
    test = '3*4+2*2'
    test = "1*2-3/4+5*6-7*8+9/10"
    print(Solution().calculate(test))  # todo, while it is collecting the 10, it still parses the zero
