def is_balanced(s):
    stack = []

    pairs = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }

    for ch in s:
        if ch in "([{":
            stack.append(ch)

        elif ch in ")]}":
            if not stack:
                return False

            if stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0

print(is_balanced("({[]})")) # True
print(is_balanced("([)]")) # False
