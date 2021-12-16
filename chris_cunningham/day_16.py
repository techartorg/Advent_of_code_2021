from io import StringIO
from math import prod

version_total = 0


def main():
    with open("inputs/day_16.txt", 'r') as f:
        data = StringIO("".join(f"{int(i, 16):04b}" for i in f.read().strip()))

    version, type_, packet = read_packet(data)
    evaluate(version, type_, packet)
    print(f"Part One: {version_total}")
    print(f"Part Two: {evaluate(version, type_, packet)}")


def read_packet(data: StringIO) -> tuple[int, int, int | list]:
    def read(bits: int) -> int:
        return int(data.read(bits), 2)

    global version_total
    version = read(3)
    version_total += version

    type_ = read(3)
    if type_ == 4:
        literal = 0
        while True:
            cont = read(1)
            literal = (literal << 4) + read(4)
            if cont == 0:
                return version, type_, literal

    i = read(1)
    if i == 0:
        length = read(15)
        target = data.tell() + length
        packets = []
        while data.tell() < target:
            packets.append(read_packet(data))
    else:
        n = read(11)
        packets = [read_packet(data) for _ in range(n)]

    return version, type_, packets


def evaluate(_: int, type_: int, val: int | list) -> int:
    match type_:
        case 0: return sum(evaluate(*i) for i in val)
        case 1: return prod(evaluate(*i) for i in val)
        case 2: return min(evaluate(*i) for i in val)
        case 3: return max(evaluate(*i) for i in val)
        case 4: return val
        case 5: return int(evaluate(*val[0]) > evaluate(*val[1]))
        case 6: return int(evaluate(*val[0]) < evaluate(*val[1]))
        case 7: return int(evaluate(*val[0]) == evaluate(*val[1]))


if __name__ == '__main__':
    main()
