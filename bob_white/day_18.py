from ast import literal_eval


def add(a, b):
    return compact([a, b])


def compact(num: list[list | int]) -> list[object]:

    exploded, new_num = explode(num)
    if exploded:
        return compact(new_num)
    spl, new_num = split(num)
    if spl:
        return compact(new_num)
    return new_num


def split(num: int | list[object]) -> tuple[bool, int | list[object]]:
    if isinstance(num, list):
        spl, left = split(num[0])
        if spl:
            return True, [left, num[1]]
        spl, right = split(num[1])
        return spl, [left, right]

    if num >= 10:
        return True, [num // 2, (num + 1) // 2]
    return False, num


def explode(num: list[object]) -> tuple[bool, list[object]]:
    num_str = str(num)
    idx = 0
    parts: list[str | int] = []  # Break the string up into either the brackets, commas, or int values
    while idx < len(num_str):
        if not num_str[idx].isdigit():
            if num_str[idx] != " ":
                parts.append(num_str[idx])
            idx += 1
            continue
        jdx = idx
        while jdx < len(num_str) and num_str[jdx].isdigit():
            jdx += 1
        parts.append(int(num_str[idx:jdx]))
        idx = jdx

    depth = 0
    for idx, c in enumerate(parts):
        if c == "[":
            depth += 1
            if depth == 5:
                left, _, right = parts[idx + 1 : idx + 4]
                assert all(isinstance(v, int) for v in (left, right))  # At this depth both values should be ints
                left_idx = right_idx = None
                for jdx, part in enumerate(parts):
                    if isinstance(part, int) and jdx < idx:  # left most int
                        left_idx = jdx
                    elif isinstance(part, int) and jdx > idx + 3 and right_idx is None:  # right most int
                        right_idx = jdx
                if right_idx is not None:
                    parts[right_idx] += right
                parts[idx : idx + 5] = [0]
                if left_idx is not None:
                    parts[left_idx] += left
                return True, literal_eval("".join(str(x) for x in parts))
        elif c == "]":
            depth -= 1

    return False, num


def magnitude(num: list[object] | int) -> int:
    if isinstance(num, list):
        a, b = num
        return 3 * magnitude(a) + 2 * magnitude(b)
    return num


puzzle = [
    literal_eval(line)
    for line in """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""".split(
        "\n"
    )
]
puzzle = [literal_eval(line) for line in open("day_18_input.txt")]
# print(puzzle)
while True:
    p1, p2, *puzzle = puzzle
    if not puzzle:
        puzzle = add(p1, p2)
        break
    puzzle.insert(0, add(p1, p2))

print(magnitude(puzzle))
# reset the puzzle, otherwise, you know, wrong answer time.
puzzle = [literal_eval(line) for line in open("day_18_input.txt")]
print(max(magnitude(add(x, y)) for x in puzzle for y in puzzle if x != y))
