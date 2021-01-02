# day 18 P1:Find every expression within (), evaluate python's eval() or my evaluate() function
# replace expression incl brackets in loop until no more brackets. Evaluate is recursive. Data
# prep: remove all spaces. P2 we can solve by modyfying the (order) and fix the end of the string

def evaluate(s):
    s = s.replace('(','').replace(')','') # don't need brackets now    
    pos = oper = -1

    for i, _ in enumerate(s): # store bracket pos, find numbers
        if i == len(s):
            return evaluate(s)
        if s.count('*') + s.count('+') <= 1:
            return eval(s)
        if pos == -1:
            pos = i # pos of 1st number
            while s[i] not in '*+':
                oper=i
                i+=1
        elif oper > -1:
            while str(s[i]).isnumeric():
                if (i := i + 1) == len(s):
                    break
            s = s.replace(str(s[pos:i]), str(evaluate(s[pos:i])), 1)

def parse(s):
    s=s.replace(' ', '')
    while True:
        sum = l_br = r_br = 0
        if s.count('(') + s.count(')') == 0: # no brackets, skip processing
            return evaluate(s)        
        for i, j in enumerate(s):
            if s[i] == '(': # store brackets position
                l_br = i
            elif s[i] == ')': # found closing bracket
                r_br = i
                sum = evaluate(s[l_br:r_br+1]) # evaluate expression
                s = s.replace(str(s[l_br:r_br+1]), str(sum), 1)
                break
    return 0

def init():
    lines = open('day18.txt').read()
    p1 = sum(parse(line) for line in lines.splitlines())
    p2 = sum(eval("("+l.replace('*',')*(') + ')+(' + "0)") for l in lines.splitlines())
    print('Part 1: {} - Part 2: {}'.format(p1, p2))

def main():
    init()

main()
