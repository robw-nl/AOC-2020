# day 18: Evaluate the expression on each line, what is the sum of the resulting values?
'''
Find every expression within brackets
evaluate with simple or complex evaluate function - replace expression incl. brakets by result
loop until no more brackets (CHECK IF THIS IS CORRECT CONDITION)

Data prep: remove all spaces

Day 2: y="("+str(open("18.txt").read()).replace('*',' ) * ( ').replace('\n',')')
'''

numbers='0123456789'

def eval_complex(s):
    # find first num, operator and second num, calculate result 
    # and go to next num op num sequence until eol is reached
    # make function recursive or call from loop?

    sum = l_num = r_num = ops = -1
    # we don't need the brackets anymore
    s=s.replace('(','').replace(')','')
    print('* START eval_complex with ', s)

    while True:
        for i, j in enumerate(s):
            # store brackets position
            # find the first numbers
 
            if i == len(s):
                return eval(s)

            if s.count('*') + s.count('+') <= 1:
                return eval(s)

            if s[i] in numbers and l_num == -1:
                l_num = i # pos of 1st number
                z = i
                while s[z] in numbers: # run through the remaining nnumers
                    z+=1 # need a temp var as we can't change i here, the loop will

            elif s[i] in '*+' and ops == -1:
                ops=z # use z as i is now wrong

            elif s[i] in numbers and ops > -1:
                while s[i] in numbers:
                    i+=1
                    if i == len(s):
                        break
                r_num = i

                # evaluate content between brackets
                part = s[l_num:r_num]

                sum = eval_complex(part)
                s = repl_strbysum(s, str(part), str(sum))
    return 0

def evaluate(s):
    print('@ START evaluate with ', s)
    
    for i, _ in enumerate(s):

        # determine if it is a simple or complex expression
        # simple: eval
        # complex call eval_complex

        try:
            # simple equation
            if s.count('*') + s.count('+')  == 1:
                return eval(s)
            # only one operator type
            elif s.count('*') == 0 and s.count('+')  > 0:
                return eval(s)
            # only one operator type
            elif s.count('+') == 0 and s.count('*')  > 0:
                return eval(s)
            else:
                return eval_complex(s)

        except:
            print('@ Error evaluation expression')
    return s

def repl_strbysum(s, strng, part):
    # use replace() function to replace all occurences of the total
    # substring by the result. Thia helps to evaluate quicker. Only
    # replace once or it will mess op the parenthesis
    return s.replace(strng, part, 1)

def parse(s):
    # find every expression within brackets
    # evaluate - replace expression incl. brakets by result
    # loop until no more brackets (CHECK IF THIS IS CORRECT CONDITION)

    print('* START PARSE with ', s)
    tot_sum = sum = l_br = r_br = 0
    while True:
        tot_sum+=sum
        if s.count('*') + s.count('+') == 1:
            print(s)
            return eval(s)
        if s.count('(') + s.count(')') == 0:
            print(s)
            return evaluate(s)

            # return evaluate(s)
        for i, j in enumerate(s):
            # store brackets position
            if s[i] == '(':
                # check following brackets
                l_br = i
            elif s[i] == ')':
                r_br = i
                # evaluate content between brackets
                part = s[l_br:r_br+1]
                sum = evaluate(part)
                s = repl_strbysum(s, str(part), str(sum))
                l_br = r_br = 0
                break
    return 0

def init():
    line = open('18.txt').read().replace('\n', ' ').replace(' ', '')
    print('Line read', line)

    sum = parse(line)
    print(sum)

def main():
    init()

main()