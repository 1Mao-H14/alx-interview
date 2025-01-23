#!/usr/bin/python3
"""Module for Prime Game.

This module contains functions to simulate a game where two players take turns
removing prime numbers and their multiples from a set of consecutive integers.
The player who cannot make a move loses the round. The module determines the
winner of multiple rounds of this game.
"""


def isWinner(x, nums):
    """isWinner

    Determine who is the winner after a certain number of rounds.

    Argumnets:
        x (int):  number of rounds
        nums (List[int]):  n's for each round.

    Return:
        (str): winnnig player
    """
    if not nums or x < 1:
        return None
    max_num = max(nums)
    rest = [True for _ in range(max(max_num + 1, 2))]
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not rest[i]:
            continue
        for j in range(i*i, max_num + 1, i):
            rest[j] = False

    rest[0] = rest[1] = False
    c = 0
    for i in range(len(rest)):
        if rest[i]:
            c += 1
        rest[i] = c

    client = 0
    for n in nums
        client += rest[n] % 2 == 1
    if client * 2 == len(nums):
        return None
    if client * 2 > len(nums):
        return "Maria"
    return "Ben"
