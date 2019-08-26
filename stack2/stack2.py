a = '2+3*4/5'
stack = []
for i in a:
    if i.isdigit():
        print(i, end='')
    else:
        stack.append(i)
# stack_reverse = stack[::-1]
for j in range(len(stack)):
    print(stack.pop(), end='')


