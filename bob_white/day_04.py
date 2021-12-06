from copy import deepcopy

stuff = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
picks, *rest = [l.strip() for l in open("day_04_input.txt")]
# picks, *rest = [l.strip() for l in stuff.split('\n')]
boards: list[list[list[str]]] = []
for line in rest:
    if not line:
        boards.append([])
    else:
        boards[-1].append(list(line.split()))
for board in boards:
    board.extend(list(z) for z in zip(*board[:]))


def find_first_board(boards: list[list[list[str]]]):
    for pick in picks.split(","):
        for idx, board in enumerate(boards):
            for line in board:
                if pick in line:
                    line.remove(pick)
                if not line:
                    return idx, int(pick)
    return -1, -1


first_boards = deepcopy(boards)
board_idx, pick = find_first_board(first_boards)
first_board = first_boards[board_idx][:5]
val = [sum(int(v) for v in l) for l in first_board]
print(sum(val) * int(pick))


def find_last_board(boards: list[list[list[str]]]) -> tuple[list[list[str]], int]:
    last_winner: list[list[str]] = []
    last_pick = ""
    winners: set[int] = set()
    for pick in picks.split(","):
        for idx, board in enumerate(boards[:]):
            if idx in winners:
                continue
            for line in board:
                if pick in line:
                    line.remove(pick)
                if not line:
                    last_winner = boards[:].pop(idx)
                    last_pick = pick
                    winners.add(idx)
                    break
    return last_winner[5:], int(last_pick)


last_board, last_pick = find_last_board(deepcopy(boards))
# The first five parts of a board (what I'm returning in the function) are the rows, if we're removing a column, the last_pick might still be in there
# so when computing the board value, we need to make sure to skip past it, this wasn't a problem in part 1 because we nuked a row before columns
# Need to do this smarter, but sleep first?
vals = [sum(int(v) for v in l if int(v) != last_pick) for l in last_board]
print(sum(vals) * last_pick)
