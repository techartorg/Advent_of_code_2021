from itertools import count, cycle
from collections import deque

player1, player2 = deque(range(1, 11)), deque(range(1, 11))
# p1.rotate(-3), p2.rotate(-7)
player1.rotate(-7), player2.rotate(-4)

s1, s2 = (0, 0)
dice = cycle(range(1, 101))
roll_cnt = 0
for turn in count(1):
    roll = [next(dice) for _ in range(3)]
    roll_cnt += 3
    if turn % 2:
        player1.rotate(-sum(roll))
        s1 += player1[0]
    else:
        player2.rotate(-sum(roll))
        s2 += player2[0]
    if s1 >= 1000 or s2 >= 1000:
        break

if s1 < s2:
    print(s1 * roll_cnt)
else:
    print(s2 * roll_cnt)


def add_point(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    a, b = [a + b for a, b in zip(x, y)]
    return a, b


def roll_dice(
    player1: int,  # Fist player's position
    player2: int,  # Second Player's position
    score1: int,  # First player's score
    score2: int,  # Second Player's score
    is_p1: bool,  # is this the first player?
    roll_sum: int,  # Sum of the rolls for this round
    rolls: int,  # what roll are we on for the round?
    _cache: dict[tuple[int, int, int, int, bool, int, int], tuple[int, int]] = {},
) -> tuple[int, int]:
    if score1 >= 21:
        return 1, 0
    if score2 >= 21:
        return 0, 1
    if (player1, player2, score1, score2, is_p1, roll_sum, rolls) not in _cache:
        wins = (0, 0)
        if rolls == 3:
            player = player1 if is_p1 else player2
            player += roll_sum
            player = ((player - 1) % 10) + 1  # easier than rotating a deque, but I liked how I did part 1
            score = score1 if is_p1 else score2
            score += player

            args = (player, player2) if is_p1 else (player1, player)
            args += (score, score2) if is_p1 else (score1, score)
            args += (not is_p1, 0, 0)  # swap players and reset roll counts
            wins = add_point(wins, roll_dice(*args))
        else:
            for i in range(1, 4):
                wins = add_point(wins, roll_dice(player1, player2, score1, score2, is_p1, roll_sum + i, rolls + 1))
        _cache[(player1, player2, score1, score2, is_p1, roll_sum, rolls)] = wins
    return _cache[(player1, player2, score1, score2, is_p1, roll_sum, rolls)]


wins = roll_dice(8, 5, 0, 0, True, 0, 0)
print(wins)
print(max(wins))
