
puzzle_input = open(__file__.replace('.py', '_input.txt')).read()

test_input = r'''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''


def parse_input(input_):
    part1 = 0
    part2 = []
    for l in input_.splitlines():
        results = parse_line(l)
        if results:
            base_score = 0
            if results[0] == ')':
                base_score = 3
            elif results[0] == ']':
                base_score = 57
            elif results[0] == '}':
                base_score = 1197
            elif results[0] == '>':
                base_score = 25137
            part1 += base_score
        else:
            results = complete_line(l)
            if results:
                score = 0
                for x in results:
                    score *= 5
                    if x == ')':
                        score += 1
                    elif x == ']':
                        score += 2
                    elif x == '}':
                        score += 3
                    elif x == '>':
                        score += 4
                part2.append(score)
    
    part2 = sorted(part2)

    return (part1, part2[int(len(part2) / 2)])



def parse_line(line):
    depth = -1
    chunks = []
    illegal_chunks = ''
    for i, x in enumerate(line):
        if x  in ['(', '[', '{', '<']:
            depth += 1
            chunks.append(x)
        if x in  [')', ']', '}', '>']:
            y = chunks[depth]
            if ( x == ')' and y == '(' or
                 x == ']' and y == '[' or
                 x == '}' and y == '{' or
                 x == '>' and y == '<' ):
                depth -= 1
                chunks.pop()
            else:
                illegal_chunks += x
    return illegal_chunks


def complete_line(line):
    depth = -1
    chunks = []
    closing = ''
    for i, x in enumerate(line):
        if x  in ['(', '[', '{', '<']:
            depth += 1
            chunks.append(x)
        if x in  [')', ']', '}', '>']:
            y = chunks[depth]
            if ( x == ')' and y == '(' or
                 x == ']' and y == '[' or
                 x == '}' and y == '{' or
                 x == '>' and y == '<' ):
                depth -= 1
                chunks.pop()
    for c in chunks[::-1]:
        if c == '(':
            closing += ')'
        elif c == '[':
            closing += ']'
        elif c == '{':
            closing += '}'
        elif c == '<':
            closing += '>'
    
    return closing


results = parse_input(test_input)
assert results[0] == 26397
assert results[1] == 288957


results = parse_input(puzzle_input)
print(f'Part One: {results[0]}\nPart Two: {results[1]}')
