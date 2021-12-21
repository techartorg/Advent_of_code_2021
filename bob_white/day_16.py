from math import prod

data = open("day_16_input.txt").read().strip()


def hex_to_bits(hex_str: str) -> str:
    # Using a comprehension so that its always padded to the 4 bit val for each character in the hex string
    return "".join(f"{int(c, 16):04b}" for c in hex_str)


def greater_than(x: list[int]) -> int:
    a, b = x
    return a > b


def less_than(x: list[int]) -> int:
    a, b = x
    return a < b


def equals(x: list[int]) -> int:
    a, b = x
    return a == b


# Need a map beause 4 is parsing the literal
operator_map = {0: sum, 1: prod, 2: min, 3: max, 5: greater_than, 6: less_than, 7: equals}

versions: list[int] = []

# returning the packet_index, and the value
def parse_packet(bits: str) -> tuple[int, int]:
    idx = 0
    versions.append(int(bits[idx : idx + 3], 2))
    idx += 3

    operator_id = int(bits[idx : idx + 3], 2)
    idx += 3
    # literals
    if operator_id == 4:
        vals: list[str] = []
        # Always at least one
        tag = bits[idx]
        idx += 1
        vals.append(bits[idx : idx + 4])
        idx += 4
        # Keep looking for more
        while tag == "1":
            tag = bits[idx]
            idx += 1
            vals.append(bits[idx : idx + 4])
            idx += 4

        val = int("".join(vals), 2)
        return idx, val

    # operator, finding sub-packets
    subs: list[int] = []

    sub_packet_type = bits[idx]
    idx += 1
    if sub_packet_type == "0":  # by length
        packet_length = int(bits[idx : idx + 15], 2)
        idx += 15
        packet_offset = idx + packet_length
        while idx < packet_offset - 6:
            offset, val = parse_packet(bits[idx:packet_offset])
            idx += offset
            subs.append(val)
    elif sub_packet_type == "1":  # by count
        packet_count = int(bits[idx : idx + 11], 2)
        idx += 11
        for _ in range(packet_count):
            offset, val = parse_packet(bits[idx:])
            idx += offset
            subs.append(val)
    # map the operator_id to an operator, and return the (idx, value)
    return idx, operator_map[operator_id](subs)


idx, value = parse_packet(hex_to_bits(data))
print("Part 1:", sum(versions))
print("Part 2:", value)
