# expression = '5 * (123 * (1 + 3) + ((4 - 3) / 6))'
expression = input()
res = []
stack = []
for i in range(len(expression)):
    if expression[i] == '(':
        stack.append(i)
    elif expression[i] == ')':
        res.append(expression[stack.pop(): i + 1])
print(*res, sep='\n')
