lines = [line.strip() for line in open("day_03_input.txt")]
counts = [sum(int(c) for c in item) for item in zip(*lines)]
gamma = int("".join("1" if c > len(lines) / 2 else "0" for c in counts), 2)
epsilon = int("".join("1" if c < len(lines) / 2 else "0" for c in counts), 2)
print(gamma * epsilon)


def get_significant_bit(lines: list[str], idx: int):
    counts = [sum(int(c) for c in item) for item in zip(*lines)]
    return "1" if counts[idx] >= (len(lines) / 2) else "0"


# Find the initial oxygen vs carbon numbers, this is the only time they start from the same search space, so after this we have to reduce them in place
oxygen: list[str] = []
carbon: list[str] = []
for line in lines:
    print(line)
    if line[0] == get_significant_bit(lines, 0):
        oxygen.append(line)
    else:
        carbon.append(line)

for idx in range(1, len(lines[0])):
    if len(oxygen) != 1:
        oxygen = [line for line in oxygen if line[idx] == get_significant_bit(oxygen, idx)]
    if len(carbon) != 1:
        carbon = [line for line in carbon if line[idx] != get_significant_bit(carbon, idx)]

print(int(carbon.pop(), 2) * int(oxygen.pop(), 2))
