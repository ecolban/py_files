from random import choice

def interpret(code):
    code = [list(l) for l in code.split('\n')]
    x, y = 0, 0
    dx, dy = 1, 0
    i = code[0][0]
    output = ''
    stack = []
    string_mode = False
    while i != '@':
        move = 1
        
        if string_mode:
            if i == '"':
                string_mode = False
            else:
                stack.append(ord(i))
        else:
        
            if i.isdigit(): stack.append(int(i))
            elif i == '+': stack[-2:] = [stack[-2] + stack[-1]]
            elif i == '-': stack[-2:] = [stack[-2] - stack[-1]]
            elif i == '*': stack[-2:] = [stack[-2] * stack[-1]]
            elif i == '/': stack[-2:] = [stack[-2] and stack[-2] / stack[-1]]
            elif i == '%': stack[-2:] = [stack[-2] and stack[-2] % stack[-1]]
            elif i == '!': stack[-1] = not stack[-1]
            elif i == '`': stack[-2:] = [stack[-2] > stack[-1]]
            elif i in '><^v?':
                if i == '?':   i = choice('><^v')
                if i == '>':   dx, dy =  1,  0
                elif i == '<': dx, dy = -1,  0
                elif i == '^': dx, dy =  0, -1
                elif i == 'v': dx, dy =  0,  1
            elif i == '_': dx, dy = (-1 if stack.pop() else 1), 0
            elif i == '|': dx, dy = 0, (-1 if stack.pop() else 1)
            elif i == '"': string_mode = True
            elif i == ':': stack.append(stack[-1] if stack else 0)
            elif i == '\\': stack[-2:] = stack[-2:][::-1]
            elif i == '$': stack.pop()
            elif i == '.': output += str(stack.pop())
            elif i == ',': output += chr(stack.pop())
            elif i == '#': move += 1
            elif i == 'p':
                ty, tx, tv = stack.pop(), stack.pop(), stack.pop()
                code[ty][tx] = chr(tv)
            elif i == 'g':
                ty, tx = stack.pop(), stack.pop()
                stack.append(ord(code[ty][tx]))
        
        for _ in range(move):
            x = (x + dx) % len(code[y])
            y = (y + dy) % len(code)
        i = code[y][x]

    return output
            
code = [['2', '>', ':', '3', 'g', '"', ' ', '"', '-', '!', 'v', '\\', ' ', ' ', 'g', '3', '0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '<']
,[' ', '|', '!', '`', '"', '&', '"', ':', '+', '1', '_', ':', '.', ':', '0', '3', 'p', '>', '0', '3', 'g', '+', ':', '"', '&', '"', '`', '|']
,[' ', '@', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '^', ' ', ' ', 'p', '3', '\\', '"', ' ', '"', ':', '<']
,['2', ' ', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8']
]
c = '\n'.join(''.join(s) for s in code)
print(c)
print(interpret(c))



