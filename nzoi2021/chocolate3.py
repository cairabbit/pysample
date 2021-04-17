import logging

logging.basicConfig(level=logging.DEBUG)

def find_max_happiness(capacities_input, num_input, func_next_student, case = 0):
    if case > 0:
        logging.debug(f'================ case {case} ================')
    logging.info(f'capacities: {capacities_input}, num: {num_input}')

    lc, rc = tolist(capacities_input)

    num = int(num_input)

    students = []
    results = []

    for i in range(0, num):
        s = tolist(func_next_student(i))
        students.append(s)
        results.append({})        

    return try_happiness(students, 0, num, lc, rc, results)

 
def try_happiness(h, i, num, lc, rc, results):
    s = h[i]
    n = s[0]
    lhs = s[1]
    rhs = s[2]
    imaxh =-1
    if i >= num - 1:
        if lhs >= 0 and lc >= n:
            imaxh = max(imaxh, lhs)
        if rhs >= 0 and rc >= n:
            imaxh = max(imaxh, rhs)
        return imaxh
    
    logging.debug(f'idx {i}, results: {results}')

    key = f'{lc}-{rc}'
    if key in results[i]:
        logging.debug(f'hit: idx {i}, return: {results[i][key]}, result: {results[i]}')
        return results[i][key]
    
    if lhs >= 0 and lc >= n:
        lrs = try_happiness(h, i+1, num, lc-n, rc, results)
        if lrs > 0:
            imaxh = max(imaxh, lhs + lrs)
    if rhs >= 0 and rc >= n:
        rrs = try_happiness(h, i+1, num, lc, rc-n, results)
        if rrs > 0:
            imaxh = max(imaxh, rhs + rrs)

    results[i][key] = imaxh
    logging.debug(f'saved: idx {i}, return: {results[i][key]}, result: {results[i]}')
    return imaxh

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
