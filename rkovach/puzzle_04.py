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


def play_bingo(numbers, boards):
    scores = copy.deepcopy(boards)

    for number in numbers:
        for i in range(len(scores)):
            b1 = score_board(scores[i], number)
            if is_board_a_winner(b1):
                return (boards[i], b1, number)
            scores[i] = b1


def play_bingo2(numbers, boards):
    winningCards = []
    winningNumbers = []
    scores = copy.deepcopy(boards)
    winningIndices = []

    for number in numbers:
        if len(scores) < 1:
            break
        for i, b in enumerate(scores):
            if i in winningIndices:
                continue
            b1 = score_board(b, number)
            if is_board_a_winner(b1):
                winningCards.append(b1)
                winningNumbers.append(number)
                winningIndices.append(i)
            else:
                scores[i] = b1

    return winningCards[-1], winningNumbers[-1]


def part_one(input_):
    numbers, board = parse_input(input_)
    winningBoard, score, number = play_bingo(numbers, board)
    finalScore = calculate_score(score, number)
    return finalScore

def part_two(input_):
    numbers, board = parse_input(input_)
    score, number = play_bingo2(numbers, board)
    finalScore = calculate_score(score, number)
    return finalScore


def calculate_score(scores, winningNumber):
    unmarkedSum = sum(sum(scores, []))
    return winningNumber * unmarkedSum


def score_board(board, number):
    #columns = list(map(list, zip(*board)))
    #print(board[0], number)
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if board[i][j] == number:
                board[i][j] = 0
    return board


def is_board_a_winner(board):
    for row in board:
        if sum(row) == 0:
            return True
    columns = list(map(list, zip(*board)))
    for c in columns:
        if sum(c) == 0:
            return True
    return False


def create_board(lines):
    board = []
    for l in lines:
        board.append([int(x) for x in l.strip().split()])
    return board

print(f'Part One: {part_one(puzzle_input)}')
print(f'Part Two: {part_two(puzzle_input)}')





assert part_one(test_input) == 4512
assert part_two(test_input) == 1924


#print(f'Part One: {}')
#print(f'Part Two: {}')