# Day 1: Report Repair
# # Part one: Multiply the two entries that sum to 2020
# Part two: What is the product of the three entries that sum to 2020

def main():
    s = [int(s.strip()) for s in open("day1.txt")]

    for a in s:
        for b in s:
            if a+b==2020:
                print(a*b)
            for c in s:
                if a+b+c==2020:
                    print(a*b*c)
                    return

if __name__ == '__main__':   
        main()
