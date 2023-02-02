 # Day 19: How many messages completely match rule 0?

def validate_rule(rules, message, seq):
    if message == '' or seq == []:
        return message == '' and seq == [] # if both are empty, True. If only one, False.
    
    r = rules[seq[0]]
    if '"' in r:
        if message[0] in r:
            return validate_rule(rules, message[1:], seq[1:]) # strip first character
        else:
            return False # wrong first character
    else:
        return any(validate_rule(rules, message, t + seq[1:]) for t in r) # expand first term

def parse_rule(rule):
    key, entry = rule.split(": ")

    if '"' not in entry:
        entry = [ [int(rule) for rule in c.split()] for c in entry.split("|") ]
    
    return (int(key),entry)


def main():
    # split the file in rules and messages
    rules_txt, messages = [lines.splitlines() for lines in open("day19.txt").read().split("\n\n")]

    # parse the rules
    rules = dict( parse_rule( rule ) for rule in rules_txt)     
    print("P1:", sum( validate_rule(rules, m, [0]) for m in messages))

    # add per aoc d19p2 instruction
    rules_txt += ["8: 42 | 42 8","11: 42 31 | 42 11 31"]

    rules = dict( parse_rule( rule ) for rule in rules_txt)
    print("P2:", sum( validate_rule(rules, m, [0]) for m in messages)) 

    
if __name__ == '__main__':   
    main()
