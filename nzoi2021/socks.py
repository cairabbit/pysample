

def check_missing(socks):
    missing = [x for x in socks if socks.count(x)<2][0]
    return missing

def main():
    socks = []
    while len(socks)<7:
        socks.append(input())
    missing = check_missing(socks)
    print(missing)


if __name__ == "__main__":
    main()

