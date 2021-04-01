import math


def count_digit(num, digit):
    nums = [int(c) for c in str(num)]
    count = 0
    for idx, val in enumerate(nums): 
        pos = len(nums) - idx
        if pos == 1:
            if val >= digit:
                count += 1
            return count

        p = 10 ** (pos - 2)
        # ones 1, tens 20, hundreds 300...
        a = (pos - 1) * p

        count += a * val
        if val > digit:
            count += 10 ** (pos - 1)
        elif val == digit:
            if pos > 1:
                rest = int(''.join([str(x) for x in nums[idx+1:]]))
                count += rest + 1

    return count

def check(x, y):
    if x == y:
        return True
    print(str(x) + '!=' + str(y))
    assert x == y

def test():
    check(count_digit(5, 3), 1)
    check(count_digit(2, 3), 0)
    check(count_digit(13, 3), 2)
    check(count_digit(34, 3), 9) 
    check(count_digit(72, 3), 17)
    check(count_digit(100, 3), 20)
    check(count_digit(133, 3), 28)
    check(count_digit(300, 3), 61)    
    check(count_digit(302, 3), 63)

def main():
    num = input()
    print(count_digit(num, 3))


if __name__ == "__main__":
    main()
