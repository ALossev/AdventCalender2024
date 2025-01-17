from collections import Counter

blinks = 75
stones = Counter([int(x) for x in open('day11.txt').read().split(' ')])

def process(s):
    if s == 0:
        return(1, -1)
    else:
        y = str(s)
        if len(y)%2 == 0:
            return(int(y[:len(y)//2]), int(y[len(y)//2:]))
        else:
            return(s * 2024, -1)
    
for b in range(blinks):
    newstones = Counter()
    for t in [(s,r) for s in stones for r in process(s) if r >= 0]:
            newstones[t[1]] += stones[t[0]]
    stones = newstones
print(sum(stones.values()))