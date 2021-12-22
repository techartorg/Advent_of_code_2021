'''
--- Day 21: Dirac Dice ---

There's not much to do as you slowly descend to the bottom of the ocean. The submarine computer challenges you to a nice game of Dirac Dice.

This game consists of a single die, two pawns, and a game board with a circular track containing ten spaces marked 1 through 10 clockwise. Each player's starting space is chosen randomly (your puzzle input). Player 1 goes first.

Players take turns moving. On each player's turn, the player rolls the die three times and adds up the results. Then, the player moves their pawn that many times forward around the track (that is, moving clockwise on spaces in order of increasing value, wrapping back around to 1 after 10). So, if a player is on space 7 and they roll 2, 2, and 1, they would move forward 5 times, to spaces 8, 9, 10, 1, and finally stopping on 2.

After each player moves, they increase their score by the value of the space their pawn stopped on. Players' scores start at 0. So, if the first player starts on space 7 and rolls a total of 5, they would stop on space 2 and add 2 to their score (for a total score of 2). The game immediately ends as a win for any player whose score reaches at least 1000.

Since the first game is a practice game, the submarine opens a compartment labeled deterministic dice and a 100-sided die falls out. This die always rolls 1 first, then 2, then 3, and so on up to 100, after which it starts over at 1 again. Play using this die.

For example, given these starting positions:

Player 1 starting position: 4
Player 2 starting position: 8

This is how the game would go:

    Player 1 rolls 1+2+3 and moves to space 10 for a total score of 10.
    Player 2 rolls 4+5+6 and moves to space 3 for a total score of 3.
    Player 1 rolls 7+8+9 and moves to space 4 for a total score of 14.
    Player 2 rolls 10+11+12 and moves to space 6 for a total score of 9.
    Player 1 rolls 13+14+15 and moves to space 6 for a total score of 20.
    Player 2 rolls 16+17+18 and moves to space 7 for a total score of 16.
    Player 1 rolls 19+20+21 and moves to space 6 for a total score of 26.
    Player 2 rolls 22+23+24 and moves to space 6 for a total score of 22.

...after many turns...

    Player 2 rolls 82+83+84 and moves to space 6 for a total score of 742.
    Player 1 rolls 85+86+87 and moves to space 4 for a total score of 990.
    Player 2 rolls 88+89+90 and moves to space 3 for a total score of 745.
    Player 1 rolls 91+92+93 and moves to space 10 for a final score, 1000.

Since player 1 has at least 1000 points, player 1 wins and the game ends. At this point, the losing player had 745 points and the die had been rolled a total of 993 times; 745 * 993 = 739785.

Play a practice game using the deterministic 100-sided die. The moment either player wins, what do you get if you multiply the score of the losing player by the number of times the die was rolled during the game?

Your puzzle answer was 757770.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

Now that you're warmed up, it's time to play the real game.

A second compartment opens, this time labeled Dirac dice. Out of it falls a single three-sided die.

As you experiment with the die, you feel a little strange. An informational brochure in the compartment explains that this is a quantum die: when you roll it, the universe splits into multiple copies, one copy for each possible outcome of the die. In this case, rolling the die always splits the universe into three copies: one where the outcome of the roll was 1, one where it was 2, and one where it was 3.

The game is played the same as before, although to prevent things from getting too far out of hand, the game now ends when either player's score reaches at least 21.

Using the same starting positions as in the example above, player 1 wins in 444356092776315 universes, while player 2 merely wins in 341960390180808 universes.

Using your given starting positions, determine every possible outcome. Find the player that wins in more universes; in how many universes does that player win?

'''
from collections import deque
import itertools

num_rolls_per_turn = 3
test_data = [ 4, 8 ]

DEBUG_1 = False
DEBUG_2 = True



def get_pos( val ):
	new_pos = -1

	while val > 10:
		val -= 10

	new_pos = val % 11

	return new_pos


def play_deterministic_dice( p1_pos, p2_pos ):
	die = deque( )
	total_die_rolls = 0

	p1_score = 0
	p2_score = 0

	turn = 0

	# Initialize the die
	for i in range( 1, 101 ):
		die.append( i )

	while p1_score < 1000 or p2_score < 1000:
		if DEBUG_1: print( 'Turn: {0}'.format( turn ) )
		# Roll the dice - P1
		result = 0
		result += sum( list( itertools.islice( die, 0, 3 ) ) ) + p1_pos
		p1_pos = get_pos( result )

		p1_score += p1_pos
		die.rotate( ( num_rolls_per_turn ) * -1 )
		total_die_rolls += num_rolls_per_turn

		if p1_score >= 1000:
			break

		if DEBUG_1: print( '\t-P1- Pos: {0:5}\tScore: {1}'.format( p1_pos, p1_score ) )

		# Roll the dice - P2
		result = 0
		result += sum( list( itertools.islice( die, 0, 3 ) ) ) + p2_pos
		p2_pos = get_pos( result )
		p2_score += p2_pos
		die.rotate( ( num_rolls_per_turn ) * -1 )
		total_die_rolls += num_rolls_per_turn

		if DEBUG_1: print( '\t-P2- Pos: {0:5}\tScore: {1}\n'.format( p2_pos, p2_score ) )

		turn += 1


	return p1_score, p2_score, total_die_rolls


def dirac_p2_turn( p1_pos, p1_score, p2_pos, p2_score, die, total_die_rolls ):
	p1_winners = 0
	p2_winners = 0

	if DEBUG_2: print( '\tRoll #{0} : {1}'.format( total_die_rolls, die[ 0 ] ) )

	# Calculate score
	old_pos = p2_pos
	p2_pos = get_pos( die[ 0 ] + p2_pos )
	p2_score += p2_pos
	if DEBUG_2: print( '\t\t-P2- Pos: {0} -> {1}\t\tScore: {2}'.format( old_pos, p2_pos, p2_score ) )

	if p2_score > 20:
		return 0, 1, total_die_rolls

	die.rotate( -1 )

	# P1 turn
	for i in range( 0, num_rolls_per_turn ):
		p1_wins, p2_wins, total_die_rolls = dirac_p1_turn( p1_pos, p1_score, p2_pos, p2_score, die.copy( ), total_die_rolls + 1 )
		p1_winners += p1_wins
		p2_winners += p2_wins
		die.rotate( -1 )

	return p1_winners, p2_winners, total_die_rolls


def dirac_p1_turn( p1_pos, p1_score, p2_pos, p2_score, die, total_die_rolls ):
	p1_winners = 0
	p2_winners = 0

	final_die_rolls = 0

	if DEBUG_2: print( '\tRoll #{0} : {1}'.format( total_die_rolls, die[ 0 ] ) )

	# Calculate score
	old_pos = p1_pos
	p1_pos = get_pos( die[ 0 ] + p1_pos )
	p1_score += p1_pos
	if DEBUG_2: print( '\t\t-P1- Pos: {0} -> {1}\t\tScore: {2}'.format( old_pos, p1_pos, p1_score ) )

	if p1_score > 20:
		return 1, 0, total_die_rolls

	die.rotate( -1 )

	# P2 turn
	for j in range( 0, num_rolls_per_turn ):
		p1_wins, p2_wins, final_die_rolls = dirac_p2_turn( p1_pos, p1_score, p2_pos, p2_score, die.copy( ), total_die_rolls + 1 )
		p1_winners += p1_wins
		p2_winners += p2_wins
		die.rotate( -1 )

	return p1_winners, p2_winners, final_die_rolls


def play_dirac_dice( p1_pos, p2_pos ):
	die = deque( )
	total_die_rolls = 0

	p1_score = 0
	p2_score = 0

	p1_winners = 0
	p2_winners = 0

	# Initialize the die
	for i in range( 1, 101 ):
		die.append( i )

	for j in range( 0, num_rolls_per_turn ):
		if DEBUG_2: print( 'Game {0}: '.format( j ) )
		p1_wins, p2_wins, total_die_rolls = dirac_p1_turn( p1_pos, p1_score, p2_pos, p2_score, die.copy( ), total_die_rolls + 1 )
		p1_winners += p1_wins
		p2_winners += p2_wins
		die.rotate( -1 )

	return p1_winners, p2_winners, total_die_rolls


def main( data ):
	answer = 0
	num_die_rolls = 0

	winner = ''
	num_universes = 0


	# Deterministic Dice
	p1_score, p2_score, num_die_rolls = play_deterministic_dice( data[ 0 ], data[ 1 ] )

	if p1_score > p2_score:
		answer = p2_score * num_die_rolls

	else:
		answer = p1_score * num_die_rolls

	# Dirac Dice
	p1_score, p2_score, num_die_rolls = play_dirac_dice( data[ 0 ], data[ 1 ] )

	if p1_score > p2_score:
		winner = 'Player 1'
		num_universes = p1_score

	else:
		winner = 'Player 2'
		num_universes = p2_score

	print( "\nLoser's score * Number of dice rolls: {0}".format( answer ) )
	print( '{0} wins in {1} universes.'.format( winner, num_universes ) )



if __name__ == "__main__":
	input = r'D:\Projects\Advent_of_Code\2021\day_21_input.txt'

	raw_data = [ ]

	with open( input, 'r' ) as input_file:
		raw_data = [ int( inst.strip( ).split( ' starting position: ' )[ 1 ] ) for inst in input_file.readlines( ) ]

	main( test_data )
