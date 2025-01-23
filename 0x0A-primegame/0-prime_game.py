#!/usr/bin/python3
"""Prime Game Module.

This module simulates a game between two players, Maria and Ben, who take turns
removing prime numbers and their multiples from a set of consecutive integers.
The player who cannot make a move loses the round. The module determines the
winner of multiple rounds of this game.
"""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game after multiple rounds.

    Args:
        x (int): The number of rounds to play.
        nums (list of int): A list of integers where each integer'n'
            a set of consecutive integers from 1 to `n`.

    Returns:
        str: The name of the player who won the most rounds ("Ben" or "Maria").
        None: If the input is invalid or the game ends in a tie.

    Example:
        >>> isWinner(3, [4, 5, 1])
        'Ben'
    """
    # Validate input
    if x <= 0 or nums is None or x != len(nums):
        return None

    # Initialize scores for Ben and Maria
    ben_wins = 0
    maria_wins = 0

    # Generate a list to mark prime numbers using the Sieve of Eratosthenes
    max_num = max(nums)
    is_prime = [1] * (max_num + 1)
    is_prime[0], is_prime[1] = 0, 0  # 0 and 1 are not prime numbers

    # Mark non-prime numbers
    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = 0

    # Play each round
    for n in nums:
        # Count the number of primes in the current set
        prime_count = sum(is_prime[0:n + 1])

        # Determine the winner of the round
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None
