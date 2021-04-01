from operator import itemgetter
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

def do_calcualtion(num, num_hurts, btn_hurts):
    plus = btn_hurts[0]
    multiply = btn_hurts[1]
    equals = btn_hurts[2]

    h = digits_hurts(num, num_hurts)
    logging.debug(f'{num} digit hurts: {h}')

    if plus >= h and multiply >= h:
        return h + equals
    
    # mulitply only
    mh = mutiply_num(num, num_hurts, h)
    mh += multiply
    if mh < h:
        h = mh

    # plus only
    ph = plus_num(num, num_hurts, h)
    ph += plus
    if ph < h:
        h = ph
    
    pmh = plus_multiply_num(num, num_hurts, h)
    pmh += plus + multiply
    if pmh < h:
        h = pmh    

    h += equals 
    logging.debug(f'hurts: {h}')   
    return h

def plus_multiply_num(num, num_hurts, h):
    for n1 in range(1, num):
        n = num - n1
        mh = mutiply_num(n, num_hurts, h)
        nh = digits_hurts(n1, num_hurts) + mh
        if nh < h:
            h = nh        
        logging.debug(f'current hurts: {h} => {num}={n1}+{n} hurts:{nh}')
    return h        

def plus_num(num, num_hurts, h):
    mid = int(num / 2)
    for n1 in range(1, mid + 1):
        n2 = num - n1
        nh = digits_hurts(n1, num_hurts) + digits_hurts(n2, num_hurts)
        if nh < h:
            h = nh        
        logging.debug(f'current hurts: {h} => {num}={n1}+{n2} hurts:{nh}')
    return h

def mutiply_num(num, num_hurts, h):
    mid = int(num**0.5)
    for n1 in range(2, mid+1):
        if num % n1 == 0:
            n2 = int(num / n1)
            nh = digits_hurts(n1, num_hurts) + digits_hurts(n2, num_hurts)
            if nh < h:
                h = nh        
            logging.debug(f'current hurts: {h} => {num}={n1}*{n2} hurts:{nh}')
    return h

def mutiply_num2(num, num_hurts, h):
    factors = factorization(num)
    logging.debug(f'{num} factors: {factors}')
    l = len(factors)
    c = 1
    while c < l:
        for i in range(0, l):
            fs = []
            fs.append(factors[i])
            j = i + 1
            while len(fs) < c and j < l:                
                fs.append(factors[j])
                j += 1
            if len(fs) < c:
                break
            n1 = 1
            for f in fs:
                n1 = n1 * f
            n2 = int(num / n1)
            nh = digits_hurts(n1, num_hurts) + digits_hurts(n2, num_hurts)
            if (nh < h):
                h = nh
            
            logging.debug(f'current hurts: {h} => {num}={n1}*{n2} hurts:{nh}')
        c+=1
    return nh

def factorization(n,m=2,a=[],count_1=0):
    for i in range(m,int(n**0.5)+1):
        if n%i==0 and i!=1:
            a.append(i)
            count_1=1
            break
    if count_1==0:
        a.append(n)
        return a
    return factorization(int(n/i),m=i,a=a)


def digits_hurts(num, num_hurts):
    ns = [int(x) for x in str(num)]
    h = 0
    for n in ns:
        h += num_hurts[n]
    return h

def main():
    num = int(input())
    num_hurts = [int(x) for x in input().split()]
    btn_hurts = [int(x) for x in input().split()]
    print(do_calcualtion(num, num_hurts, btn_hurts))

if __name__ == "__main__":
    main()