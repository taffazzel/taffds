import itertools
import random
import string

list1 = list("AABBBCCCAA")
'''for k, g in itertools.groupby(list1):
    print(k,len(list(g)))'''
l=[]
for k, g in itertools.groupby(list1):
    l.append(k+str(len(list(g))))
l2 = "".join(x for x in l)
print(l2)


""" Instructions to candidate.

1. A basic string compression operation works by counting sequences of repeating characters and stores this as one character and a count.
Given "AABBBCCCD" it should return "A2B3C3D1". 

Sample Input:
AABBBCCCD
ABCDE
KKKKK

Sample Output:
A2B3C3D1
A1B1C1D1E1
K5

2. Consider adding further tests to runTests
3. Implement the function compressString correctly
"""
import itertools
def compressString(s_in):
    l=[]
    for k, g in itertools.groupby(list(s_in)):
        l.append(k+str(len(list(g))))
    return_list = "".join(x for x in l)
    return return_list

def runTests():
    """ Returns True if all tests pass. Otherwise returns False. """
    tests = [["AABBBCCCD", "A2B3C3D1"],
             ["ABCDE", "A1B1C1D1E1"],
             ["AABBBCCCDAABB", "A2B3C3D1A2B2"],
             ["KKKKK", "K5"]]

    for test in tests:
        if not (compressString(test[0]) == test[1]):
            return False
    return True

def main():
    if (runTests()):
        print( "Test(s) passed")
    else:
        print( "Test(s) failed")

if __name__ == '__main__':
    main()

"""
You are given coins of different denominations and a total amount of money. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

E.g. for the sample coins array {1,5,10,25} the value 55 could be made up of 3 coins, 5 (1x) and 25 (2x)

"""
import pytest


def coinChange(coins, amount):
    # TODO: implement here
    if amount == 0:
        print("if amount zero")
        number_of_coins_after_round = 0
    else:
        print("if amount non zero")
        lowest = []
        for val in coins:
            total_number_of_coins = amount / val
            lowest.append(total_number_of_coins)
        number_of_coins_after_round = round(min(lowest)) + 1
    return number_of_coins_after_round


def test():
    # TODO you can add additional test cases here
    testCases = [
        [[[1, 5, 10, 25], 55], 3],
        [[[1, 5, 10, 25], 56], 4],
        [[[1, 2, 3], 0], 0],
        #   [ [ [2]         , 7  ],-1],
        [[[1, 3, 4], 6], 2],
    ]
    for test in testCases:
        coins = test[0][0]
        amount = test[0][1]
        required = test[1]
        assert coinChange(coins, amount) == required


def main():
    pytest.main(["-v"])


if __name__ == '__main__':
    main()

# Q: Use a single list comprehension to create a unique list of tuples of all possible tshirt combinations,
# where each combination is in stock

tshirt_sizes = ['S', 'M', 'L', 'XL']
colours = ['black', 'black', 'white', 'blue', 'blue', 'green', 'yellow', 'red']
out_of_stock = [('S', 'blue'), ('M', 'green'), ('M', 'red'), ('XL', 'white')]

'''
1. Create a combination of tshirt_sizes and colours.
2. Then subtract the out of stock from the above whole set of possible combination received above
'''

list_of_stock = []
for size in tshirt_sizes:
    for colour in colours:
        list_of_stock.append((size, colour))


# Q: Explain the purpose of the following class, including the use of the @staticmethod and @property decorators- Singleton pattern

class AppContext:
    _instance = None

    @staticmethod
    def get_instance():
        if AppContext._instance is None:
            raise Exception()
        return AppContext._instance

    def __init__(self, args):
        if AppContext._instance is not None:
            raise Exception()
        self._config = args.config
        AppContext._instance = self

    @property
    def config(self):
        return self._config


# Q: How can we make these functions run in parallel?

def print_numbers():
    for i in range(500000):
        print(i)


def print_letters():
    for i in range(500000):
        letter = random.choice(string.ascii_uppercase)
        print(letter)



