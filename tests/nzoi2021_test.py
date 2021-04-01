from nzoi2021.socks import *
from nzoi2021.mine_reader import *
from nzoi2021.count_digit import *
from nzoi2021.caldulator import *
from nzoi2021.chocolate import *
from nzoi2021.chocolate2 import find_max_happiness as find_max_happiness2

def test_chocolate2():
    case = 1
    assert find_max_happiness2("3 3", "1", lambda i: [
        "3 1 6"
        ][i], case) == 6
    case += 1
    assert find_max_happiness2("3 3", "2", lambda i: [
        "3 -1 6",
        "2 8 -1"
        ][i], case) == 14
    case += 1
    assert find_max_happiness2("4 6", "3", lambda i: [
        "3 1 6",
        "2 6 4",
        "2 5 -1"
        ][i], case) == 17
    case += 1
    assert find_max_happiness2("9 6", "5", lambda i: [
        "5 9 8",
        "6 12 4",
        "3 9 44",
        "4 8 20",
        "2 12 5"
        ][i], case) == -1
    case += 1
    assert find_max_happiness2("9 6", "5", lambda i: [
        "1 9 8",
        "3 12 4",
        "3 9 44",
        "4 8 20",
        "2 12 5"
        ][i], case) == 84
    case += 1
    assert find_max_happiness2("9 6", "5", lambda i: [
        "1 9 8",
        "3 12 12",
        "3 9 44",
        "4 20 20",
        "2 12 5"
        ][i], case) == 97
    case += 1
    assert find_max_happiness2("9 6", "5", lambda i: [
        "1 9 8",
        "3 20 20",
        "3 9 44",
        "4 20 20",
        "2 12 5"
        ][i], case) == 105
    case += 1
    assert find_max_happiness2("9 6", "5", lambda i: [
        "1 9 8",
        "3 18 18",
        "3 44 44",
        "4 20 20",
        "2 12 5"
        ][i], case) == 103
    case += 1
    assert find_max_happiness2("9 4", "5", lambda i: [
        "1 9 8",
        "3 18 18",
        "3 44 44",
        "4 20 20",
        "2 12 5"
        ][i], case) == 103
    case += 1
    assert find_max_happiness2("9 4", "5", lambda i: [
        "1 9 8",
        "3 18 18",
        "3 44 44",
        "3 20 20",
        "2 12 5"
        ][i], case) == 103
    case += 1
    assert find_max_happiness2("9 4", "5", lambda i: [
        "1 9 8",
        "4 -1 18",
        "3 44 44",
        "3 20 20",
        "2 12 5"
        ][i], case) == 103
    case += 1
    assert find_max_happiness2("9 4", "5", lambda i: [
        "1 9 8",
        "4 18 -1",
        "3 44 44",
        "3 20 20",
        "2 12 5"
        ][i], case) == 102
    case += 1
    assert find_max_happiness2("9 4", "5", lambda i: [
        "1 9 8",
        "4 18 16",
        "3 44 44",
        "3 20 20",
        "2 12 5"
        ][i], case) == 12+8+44+20+18
    case += 1
    assert find_max_happiness2("15 4", "6", lambda i: [
        "3 9 8",
        "4 18 1",
        "3 0 44",
        "3 12 20",
        "3 20 20",
        "3 12 5"
        ][i], case) == 9+1+0+12+20+12

def test_chocolate():
    i = 1
    assert find_max_happiness(tolist("3 3"), 1, [
        tuple(tolist("3 1 6"))
        ], i) == 6
    i += 1
    assert find_max_happiness(tolist("3 3"), 2, [
        tuple(tolist("3 -1 6")),
        tuple(tolist("2 8 -1"))
        ], i) == 14
    i += 1
    assert find_max_happiness(tolist("4 6"), 3, [
        tuple(tolist("3 1 6")),
        tuple(tolist("2 6 4")),
        tuple(tolist("2 5 -1"))
        ], i) == 17
    i += 1
    assert find_max_happiness(tolist("9 6"), 5, [
        tuple(tolist("1 9 8")),
        tuple(tolist("3 12 4")),
        tuple(tolist("3 9 44")),
        tuple(tolist("4 8 20")),
        tuple(tolist("2 12 5"))
        ], i) == 84
    i += 1
    assert find_max_happiness(tolist("9 6"), 5, [
        tuple(tolist("1 9 8")),
        tuple(tolist("3 12 12")),
        tuple(tolist("3 9 44")),
        tuple(tolist("4 20 20")),
        tuple(tolist("2 12 5"))
        ], i) == 97
    i += 1
    assert find_max_happiness(tolist("9 6"), 5, [
        tuple(tolist("1 9 8")),
        tuple(tolist("3 20 20")),
        tuple(tolist("3 9 44")),
        tuple(tolist("4 20 20")),
        tuple(tolist("2 12 5"))
        ], i) == 105
    i += 1
    assert find_max_happiness(tolist("9 6"), 5, [
        tuple(tolist("1 9 8")),
        tuple(tolist("3 18 18")),
        tuple(tolist("3 44 44")),
        tuple(tolist("4 20 20")),
        tuple(tolist("2 12 5"))
        ], i) == 103
    i += 1
    assert find_max_happiness(tolist("9 4"), 5, [
        tuple(tolist("1 9 8")),
        tuple(tolist("3 18 18")),
        tuple(tolist("4 44 44")),
        tuple(tolist("3 20 20")),
        tuple(tolist("2 12 5"))
        ], i) == 103
    i += 1
    assert find_max_happiness(tolist("9 4"), 5, [
        tuple(tolist("1 9 8")),
        tuple(tolist("4 18 18")),
        tuple(tolist("3 44 44")),
        tuple(tolist("3 20 20")),
        tuple(tolist("2 12 5"))
        ], i) == 103
    i += 1
    assert find_max_happiness(tolist("9 4"), 5, [
        tuple(tolist("1 9 8")),
        tuple(tolist("4 -1 18")),
        tuple(tolist("3 44 44")),
        tuple(tolist("3 20 20")),
        tuple(tolist("2 12 5"))
        ], i) == 103
    i += 1
    assert find_max_happiness(tolist("9 4"), 5, [
        tuple(tolist("1 9 8")),
        tuple(tolist("4 18 -1")),
        tuple(tolist("3 44 44")),
        tuple(tolist("3 20 20")),
        tuple(tolist("2 12 5"))
        ], i) == 102
    i += 1
    assert find_max_happiness(tolist("9 4"), 5, [
        tuple(tolist("1 9 8")),
        tuple(tolist("4 18 16")),
        tuple(tolist("3 44 44")),
        tuple(tolist("3 20 20")),
        tuple(tolist("2 12 5"))
        ], i) == 12+8+44+20+18
    i += 1
    assert find_max_happiness(tolist("15 4"), 6, [
        tuple(tolist("3 9 8")),
        tuple(tolist("4 18 1")),
        tuple(tolist("3 0 44")),
        tuple(tolist("3 12 20")),
        tuple(tolist("3 20 20")),
        tuple(tolist("3 12 5"))
        ], i) == 9+1+0+12+20+12



def test_calculator():
    assert do_calcualtion(12, [5,10,6,8,1,2,6,9,3,4], [6,1000,2]) == 12
    assert do_calcualtion(12, [10,10,1,2,10,3,10,10,10,10], [0,0,0]) == 5

def test_count_digit():
    assert count_digit(5, 3) == 1
    assert count_digit(2, 3) == 0
    assert count_digit(13, 3) == 2
    assert count_digit(34, 3) == 9
    assert count_digit(72, 3) == 17
    assert count_digit(100, 3) == 20
    assert count_digit(133, 3) == 28
    assert count_digit(300, 3) == 61
    assert count_digit(302, 3) == 63

def test_mine_reader():
    assert do_mine_reader('10', 'hearts') == 4
    assert do_mine_reader('K', 'diamonds') == 14


def test_socks():
    assert check_missing(['a','a', 'b'])=='b'
