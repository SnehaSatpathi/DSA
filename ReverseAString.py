def reverse_string(s):
    stack = []
    for ch in s:
        stack.append(ch)
    result = ""
    while stack:
        result += stack.pop()
    return result
print(reverse_string("hello"))