
suits = ['spades', 'clubs', 'diamonds', 'hearts']
nums = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def do_mine_reader(n, s):
    si = suits.index(s)
    h = (len(suits) - si - 1) * len(nums)
    n = len(nums) - nums.index(n) - 1
    return h + n


def main():
    n = input()
    s = input()
    print(do_mine_reader(n, s))

if __name__ == "__main__":
    main()


    