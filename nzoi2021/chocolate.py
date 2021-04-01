import logging

logging.basicConfig(level=logging.DEBUG)

import time

def find_max_happiness(capacities, num, happiness, case=0):
    if case > 0:
        tic = time.perf_counter()
        logging.info('==================== case ' + str(case) + ' ====================')
    for d, v in enumerate(happiness):
        logging.info(str(d) + ':' + str(v))

    lc = capacities[0]
    rc = capacities[1]

    logging.info(f'left: {lc}, right: {rc}')

    t = sum([x[0] for x in happiness])
    if t > lc + rc:
        return -1

    lsh = [x for x in happiness if x[2]==-1]
    rsh = [x for x in happiness if x[1]==-1]
    
    lt = sum([x[0] for x in lsh])
    if lt > lc:
        return -1
    rt = sum([x[0] for x in rsh])
    if rt > rc:
        return -1
    
    lhs = sum([x[1] for x in lsh])
    rhs = sum([x[2] for x in rsh])

    lc = lc - lt
    rc = rc - rt
    ths = lhs + rhs

    h = [x for x in happiness if x[1]!=-1 and x[2]!=-1]
    if len(h) > 0:
        h.sort(key = lambda x: -x[0])
        max = try_happiness3(h, 0, lc, rc)
        ths += max
        
    logging.info('max: ' + str(ths))
    if case > 0:
        toc = time.perf_counter()
        logging.info(f"running in {toc - tic:0.4f} seconds")
    return ths 
        
def try_happiness(h, i, lc, rc):
    s = h[i]
    n = s[0]
    lhs = s[1]
    rhs = s[2]
    if i >= len(h) - 1:
        if lc >= n and rc >= n:
            return max(lhs, rhs)
        elif lc >= n:
            return lhs
        elif rc >= n:
            return rhs
        else:
            return -1
    
    if lc >= n and rc >= n:
        lrs = try_happiness(h, i+1, lc-n, rc)
        rrs = try_happiness(h, i+1, lc, rc-n)
        if lrs > 0 and rrs > 0:
            return max(lhs + lrs, rhs + rrs)
        elif lrs > 0:
            return lhs + lrs
        elif rrs > 0:
            return rhs + rrs
    elif lc >= n:
        lrs = try_happiness(h, i+1, lc-n, rc)
        if lrs > 0:
            return lhs + lrs       
    elif rc >= n:
        rrs = try_happiness(h, i+1, lc, rc-n)
        if rrs > 0:
            return rhs + rrs

    return -1

def try_happiness2(h, i, lc, rc):
    stack = []
    stack.append((i, h[i], lc, rc, 0)) # 0 max happiness
    last = len(h) - 1
    maxh = -1
    k = 1
    while len(stack) > 0:        
        logging.debug('k:' + str(k))
        for d, v in enumerate(stack):
            logging.debug(str(d) + ':' + str(v))
        k+=1

        s = stack.pop()
        i = s[0]
        hi = s[1]
        lc = s[2]
        rc = s[3]
        mh = s[4]

        n = hi[0]
        lhs = hi[1]
        rhs = hi[2]
        if i >= last:
            if lc >= n and rc >= n:
                mh += max(lhs, rhs)
            elif lc >= n:
                mh += lhs
            elif rc >= n:
                mh += rhs
            else:
                mh = -1
            if mh > maxh:
                maxh = mh
                
            logging.info('mh:' + str(mh) + ', max:' + str(maxh))
        else:
            if lc >= n and rc >= n:
                stack.append((i+1, h[i+1], lc - n, rc, mh + lhs))
                stack.append((i+1, h[i+1], lc, rc - n, mh + rhs))
            elif lc >= n:
                stack.append((i+1, h[i+1], lc - n, rc, mh + lhs))       
            elif rc >= n:
                stack.append((i+1, h[i+1], lc, rc - n, mh + rhs))

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
    capacities = tolist(input())
    num = int(input())
    hs = []
    for i in range(0, num):
        h = tuple(tolist(input()))
        hs.append(h)
    r = find_max_happiness(capacities, num, hs)
    if r < 0:
        print('Camp is cancelled')
    else:
        print(r)


if __name__ == "__main__":
    main()
