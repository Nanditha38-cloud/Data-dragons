def calculate(expression: str) -> float:
    expression = expression.replace(" ", "")
    stack = []
    num = 0
    sign = '+'

    for i in range(len(expression)):
        char = expression[i]

        if char.isdigit():
            num = num * 10 + int(char)

        if char in "+-*/" or i == len(expression) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                stack.append(stack.pop() / num)

            sign = char
            num = 0

    return round(sum(stack), 2)


# Sample Tests
assert calculate("2 + 3") == 5.0
assert calculate("10 - 5 * 2") == 0.0
assert calculate("20 / 4 + 3 * 2") == 11.0
assert calculate("100 / 3") == 33.33
assert calculate("5") == 5.0
