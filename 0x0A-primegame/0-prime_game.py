#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """function finding the final winner"""
    winCounter = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        roundWinner = isRoundWinner(nums[i], x)
        if roundWinner is not None:
            winCounter[roundWinner] += 1

    if winCounter['Maria'] > winCounter['Ben']:
        return 'Maria'
    elif winCounter['Ben'] > winCounter['Maria']:
        return 'Ben'
    else:
        return None


def isRoundWinner(n, x):
    """function finding the round winner"""
    list = [i for i in range(1, n + 1)]
    players = ['Maria', 'Ben']

    for i in range(n):
        currentPlayer = players[i % 2]
        choices = []
        prime = -1
        for idx, num in enumerate(list):
            if prime != -1:
                if num % prime == 0:
                    choices.append(idx)
            else:
                if isPrime(num):
                    choices.append(idx)
                    prime = num
        if prime == -1:
            if currentPlayer == players[0]:
                return players[1]
            else:
                return players[0]
        else:
            for idx, val in enumerate(choices):
                del list[val - idx]
    return None


def isPrime(n):
    if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
        return False
    else:
        for i in range(3, int(n**(1/2))+1, 2):
            if n % i == 0:
                return "Not prime"
        return True
