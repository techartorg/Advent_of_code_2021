from copy import copy
from pathlib import Path
from typing import List, Optional, Tuple


def _calculate_score(card: List[List[str]], number: str) -> None:
    unmarked_num_val = 0
    for row in card:
        unmarked_num_val += sum([int(x) for x in row if not x.endswith('*')])

    print( unmarked_num_val * int(number))


def _score_card(card: List[List[str]]) -> Tuple[bool, List[List[str]]]:
    row_complete = False
    column_complete = False
    
    # Row
    for row in card:
        row_complete = all([x.endswith('*') for x in row])
        if row_complete:
            break
    
    if not row_complete:
        for i in range(len(card[0])):
            column = [r[i] for r in card]
            column_complete = all([x.endswith('*') for x in column])
            if column_complete:
                break

    return any([row_complete, column_complete]), card


def _stamp_card( number: str, card: List[List[str]]) -> Tuple[bool, List[List[str]]]:
    success = False
    for i, row in enumerate(card):
        if number in row:
            idx = row.index(number)
            if not row[idx].endswith('*'):
                row[idx] = row[idx] + '*'
                card[i] = row
            
            success, card = _score_card(card)
            if success:
                break

    return success, card


def part_1( bingo_numbers: List[str], bingo_cards: List[List[List[str]]]) -> None:
    for number in bingo_numbers:
        for i, bc in enumerate(bingo_cards):
            success, bc = _stamp_card(number, bc)
            bingo_cards[i] = bc
            if success:
                _calculate_score( bc, number)
                return


def part_2( bingo_numbers: List[str], bingo_cards: List[List[List[str]]]) -> None:
    cards_in_play = list(range(len(bingo_cards)))
    last_winning_combo = None
    for number in bingo_numbers:
        for i, bc, in enumerate(bingo_cards):
            if i in cards_in_play:
                success, bc = _stamp_card(number, bc)
                bingo_cards[i] = bc
                if success:
                    last_winning_combo = (bc, number)
                    cards_in_play.remove(i)            

    if last_winning_combo:
        _calculate_score(*last_winning_combo)


if __name__ == "__main__":
    filepath = Path(__file__).parent / "day_04_input.txt"
    data = filepath.read_text().splitlines()
    bingo_numbers = [x for x in data.pop(0).split(',')]
    data.pop(0)
    
    bingo_cards = []
    bingo_card = []
    for x in data:
        if not x:
            bingo_cards.append(copy(bingo_card))
            bingo_card.clear()
            continue

        row = [n for n in x.split( ) if n]
        bingo_card.append(row)
    
    # To cover for there not being a blank line at the end of the data
    if bingo_card:
        bingo_cards.append(copy(bingo_card))

    part_1(bingo_numbers, bingo_cards)
    part_2(bingo_numbers, bingo_cards)

