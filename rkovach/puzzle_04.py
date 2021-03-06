r'''
--- Day 4: Giant Squid ---
You're already almost 1.5km (almost a mile) below the surface of the ocean, 
already so deep that you can't see any sunlight. What you can see, however, 
is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. 
Numbers are chosen at random, and the chosen number is marked on all boards 
on which it appears. (Numbers may not appear on all boards.) If all numbers 
in any row or any column of a board are marked, that board wins. (Diagonals 
don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and 
the giant squid) pass the time. It automatically generates a random order 
in which to draw numbers and a random set of boards (your puzzle input). 

For example:

    7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

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
     2  0 12  3  7

After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no 
winners, but the boards are marked as follows (shown here adjacent to each 
other to save space):

    22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
     8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
    21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
     6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
     1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are 
still no winners:

    22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
     8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
    21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
     6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
     1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

Finally, 24 is drawn:

    22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
     8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
    21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
     6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
     1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

At this point, the third board wins because it has at least one complete row 
or column of marked numbers (in this case, the entire top row is marked: 
14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the 
sum of all unmarked numbers on that board; in this case, the sum is 188. 
Then, multiply that sum by the number that was just called when the board 
won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will 
win first. What will your final score be if you choose that board?


--- Part Two ---
On the other hand, it might be wise to try a different strategy: let the 
giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so 
rather than waste time counting its arms, the safe thing to do is to figure 
out which board will win last and choose that one. That way, no matter which 
boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens 
after 13 is eventually called and its middle column is completely marked. 
If you were to keep playing until this point, the second board would have a 
sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final 
score be?

'''

import copy

test_input = r'''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

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
 2  0 12  3  7
'''

puzzle_input = open(__file__.replace('.py', '_input.txt')).read()

def parse_input(input_):
    """
    The first line are the bingo numbers to call. 
    The rest are the bingo cards separated by empty lines.

    """
    lines = input_.splitlines()
    numbers = [int(x) for x in lines[0].strip().split(',')]
    boards = []

    i = 2
    for l in lines[2::6]:
        if l == '':
            continue
        b = create_board(lines[i:i+5])
        boards.append(b)
        i += 6
    
    return numbers, boards


def create_board(lines):
    """Convert the board into a list of lists.
    
    For example::
        [[ 2, 77,  1, 37, 29],
         [50,  8, 87, 12, 76],
         [74, 88, 48, 60, 79],
         [41, 35, 92, 33, 34],
         [45, 52, 75, 24, 28]]
    
    """
    board = []
    for l in lines:
        board.append([int(x) for x in l.strip().split()])
    return board


def score_board(board, number):
    """
    Check the board for the number and replace it with -1.
    Update the board and return it.

    """
    winner = False
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if board[i][j] == number:
                board[i][j] = -1

                # check to see if the number completes a row or column.
                if sum(row) == -5 or sum([row[j] for row in board]) == -5:
                    winner = True
    return board, winner


def calculate_score(board, winningNumber):
    """
    Score is the sum of the unmarked squares multiplied
    by the winning number.
    
    """
    unmarkedSum = 0
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            # marked squares have a value of -1, clamp them to zero.
            unmarkedSum += max(0, board[i][j])
    return winningNumber * unmarkedSum


def play_bingo(numbers, boards):
    """
    Iterate through the numbers, then iterate through the boards.
    Once a board has won, remove it from the list and keep playing
    with the remaining boards.
    Each time a board wins, add it and the winning number to a list
    so we can track the order of wins. We eventually need the first
    board to win and the last board to win as well as their respective
    winning numbers.

    """
    winningCards = []
    winningNumbers = []
    winningIndices = []

    scores = copy.deepcopy(boards)
    for number in numbers:
        for i, b in enumerate(scores):
            # skip cards that already won.
            if i in winningIndices:
                continue
            b1, winner = score_board(b, number)
            if winner:
                winningCards.append(b1)
                winningNumbers.append(number)
                winningIndices.append(i)
            else:
                # update the board for the next round.
                scores[i] = b1

    return (winningCards, winningNumbers)


def solve(input_):
    numbers, board = parse_input(input_)
    score, number = play_bingo(numbers, board)
    part1_answer = calculate_score(score[0], number[0])
    part2_answer = calculate_score(score[-1], number[-1])
    return (part1_answer, part2_answer)


test_answers = solve(test_input)
assert test_answers[0] == 4512
assert test_answers[1] == 1924


puzzle_answers = solve(puzzle_input)
print(f'Part One: {puzzle_answers[0]}')
print(f'Part Two: {puzzle_answers[1]}')