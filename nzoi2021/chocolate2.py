import logging

logging.basicConfig(level=logging.DEBUG)

def find_max_happiness(capacities_input, num_input, func_next_student, case = 0):
    if case > 0:
        logging.debug(f'================ case {case} ================')
    logging.info(f'capacities: {capacities_input}, num: {num_input}')

    capacities = tolist(capacities_input)
    lc = capacities[0]
    rc = capacities[1]

    num = int(num_input)

    hs = []
    total = 0
    left_only = 0
    right_only = 0
    maxh = 0

    for i in range(0, num):
        s = tolist(func_next_student(i))
        n = s[0]
        lh = s[1]
        rh = s[2]
        total += n
        
        if total > lc + rc or maxh == -1:
            maxh = -1
            continue

        if rh == -1:
            if lc >= n:
                maxh += lh
                lc -= n
                total -= n
            else:
                maxh = -1
                continue  
        elif lh == -1:
            if rc >= n:
                maxh += rh
                rc -= n
                total -= n
            else:
                maxh = -1
                continue   
        else:
            hs.append(s)

    if maxh >= 0 and len(hs)>0:
        maxh += try_happiness3(hs, 0, lc, rc)
    
    return maxh

 
def try_happiness3(h, idx, lc, rc):
    hs = []
    for i in range(idx, len(h)):
        s = h[i]
        logging.debug(f'-------{i}------------')
        logging.debug(s)
        num = s[0]
        lh = s[1]
        rh = s[2]        
        toBeRemoved = []
        if len(hs) <= 0:
            if lc >= num:
                hs.append((lc-num, rc, lh))
            if rc >= num:
                hs.append((lc, rc-num, rh))
        else:
            hs = [x for x in hs if x[0]>=num or x[1]>=num]
            for j in range(0, len(hs)):
                rs = hs[j]
                lnum = rs[0]
                rnum = rs[1]
                hv = rs[2]
                changed = False
                if lnum >= num:
                    hs[j] = (lnum - num, rnum, hv + lh)
                    changed = True
                if rnum >= num:
                    if changed:
                        hs.append((lnum, rnum - num, hv + rh))
                    else:
                        hs[j] = (lnum, rnum - num, hv + rh)
                    changed = True                
                if not changed:
                    toBeRemoved.append(rs)
        if len(toBeRemoved) > 0:
            for x in toBeRemoved:
                hs.remove(x)
        logging.debug(hs)
    maxh = -1
    if len(hs) > 0:
        maxh = max([x[2] for x in hs])
    logging.info(f'max: {maxh}')

    return maxh

def tolist(l):
    return [int(x) for x in l.split()]

def main():
    def get_next_student(i):
        return input()
    r = find_max_happiness(input(), input(), get_next_student)
    if r < 0:
        print('Camp is cancelled')
    else:
        print(r)


if __name__ == "__main__":
    main()
