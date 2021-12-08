test_input = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
'''

puzzle_input = open(__file__.replace('.py', '_input.txt')).read()


def part_one(input_):
    counter = 0
    for l in input_.splitlines():
        tokens = l.split()
        signals = tokens[0:10]
        output = tokens[-4:]
        for number in output:
            wire_count = len(number)
            if wire_count in [2, 3, 4, 7]:
                counter += 1
    return counter

def part_two(input_):
    total_value = 0
    for l in input_.splitlines():

        tokens = l.split()
        signals = tokens[0:10]
        signals = [''.join(sorted(x)) for x in signals]
        output = tokens[-4:]
        output = [''.join(sorted(x)) for x in output]

        numbers = {0: None, 
                   1: None, 
                   2: None, 
                   3: None, 
                   4: None, 
                   5: None, 
                   6: None, 
                   7: None, 
                   8: None, 
                   9: None}
        
        zero_six_nine = []
        two_five_three = []

        for number in signals:
            if len(number) == 2:
                numbers[1] = number
            elif len(number) == 3:
                numbers[7] = number
            elif len(number) == 4:
                numbers[4] = number
            elif len(number) == 7:
                numbers[8] = number
            elif len(number) == 6:
                zero_six_nine.append(number)
            elif len(number) == 5:
                two_five_three.append(number)
            else:
                raise
        
        for num in zero_six_nine:
            # The "6" digit will only share one wire with the "1" digit, so we
            # can determine which number with 6 wires is the number 6.
            if len(set(num).intersection(set(numbers[1]))) == 1:
                numbers[6] = num

            # The "9" digit can be found by overlapping the wire with
            # the "4" digit.
            elif len(set(num).intersection(set(numbers[4]))) == 4:
                numbers[9] = num
            
            else:
                numbers[0] = num
        
        for num in two_five_three:
            # The "3" digit will overlap with the "1"
            if len(set(num).intersection(set(numbers[1]))) == 2:
                numbers[3] = num
            
            # The "5" digit will overlap the "6" digit.
            elif len(set(num).intersection(set(numbers[6]))) == 5:
                numbers[5] = num
            
            else:
                numbers[2] = num
        
        # reverse the dictionary mapping to convert back to integers.
        mappings = {}
        for k, v in numbers.items():
            mappings[v] = str(k)

        output_number = ''.join([mappings[x] for x in output])
        total_value += int(output_number)
    
    return total_value


print(part_one(puzzle_input))
print(part_two(puzzle_input))
