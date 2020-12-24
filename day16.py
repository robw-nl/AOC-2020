from itertools import chain

ranges = ((31,201),(227,951),(49,885),(892,961),(36,248),(258,974),
            (37,507),(527,965),(37,331),(351,970),(38,370),(382,970),
            (33,686),(711,960),(46,753),(775,953),(34,138),(154,959),
            (26,167),(181,961),(43,664),(675,968),(47,603),(620,954),
            (40,290),(313,972),(37,792),(799,972),(32,97 ),(115,954),
            (25,916),(942,966),(39,572),(587,966),(25,834),(858,953),
            (48,534),(544,959),(47,442),(463,969))


codes = set(chain(*(range(start, end+1) for start, end in ranges)))


lines = open('day16a.txt').read().split('\n')
cF=tF=0
for line in lines:
    l=line.split(',')

    for i in l:      
        if int(i) not in codes:
            cF+=int(i)
            tF+=1
        
print('Nr', tF,'Sum', cF)