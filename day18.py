# day 18: Evaluate the expression on each line, what is the sum of the resulting values?
'''
Find every expression within (), evaluate python's eval() or my evaluate() function - replace expression
incl brackets in loop until no more brackets. Evaluate is recursive. Data prep: remove all spaces
'''

def repl_strbysum(s, strng, part):
    return s.replace(strng, part, 1)

def evaluate(s):
    s = s.replace('(','').replace(')','') # don't need brackets now    
    numbers = '0123456789'
    l_num = ops = -1

    for i, _ in enumerate(s): # store bracket positions, find the first numbers
        if i == len(s):
            return evaluate(s)
        if s.count('*') + s.count('+') <= 1:
            return eval(s)
        if s[i] in numbers and l_num == -1:
            l_num = i # pos of 1st number
            shift = i
            while s[shift] in numbers: # run through the remaining numbers
                shift+=1 # use a tmp var: we loop quicker than for loop controlled i
        elif s[i] in '*+':
            ops=shift # use shift as i is now wrong as we just traversed through chars
        elif s[i] in numbers and ops > -1:
            while s[i] in numbers:
                i+=1
                if i == len(s):
                    break
            part = s[l_num:i] # evaluate content between brackets
            s = repl_strbysum(s, str(part), str(evaluate(part)))

def parse(s):
    s=s.replace(' ', '')
    while True:
        sum = l_br = r_br = 0
        if s.count('(') + s.count(')') == 0: # no brackets, skip processing
            return evaluate(s)
            
        for i, j in enumerate(s):
            if s[i] == '(': # store brackets position
                l_br = i # check following brackets
            elif s[i] == ')':
                r_br = i # evaluate content between brackets
                part = s[l_br:r_br+1]
                sum = evaluate(part)
                s = repl_strbysum(s, str(part), str(sum))
                break
    return 0

def init():
    lines = open('day18.txt').read()

    s = sum(parse(line) for line in lines.splitlines())
    t = eval("("+lines.replace('*',')*(').replace('\n',')+(')+"0)")

    print('Part 1: {} - Part 2: {}'.format(s, t))

def main():
    init()

main()
