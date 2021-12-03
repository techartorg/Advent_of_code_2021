

lines = [line.strip() for line in open('day_03_input.txt')]
counts = [sum(int(c) for c in item) for item in zip(*lines)]
gamma = int(''.join('1' if c > len(lines)/2 else '0' for c in counts),2)
epsilon = int(''.join('1' if c < len(lines)/2 else '0' for c in counts), 2)
print(gamma * epsilon)


def get_significant_bit(lines, idx, ox=True):
    counts = [sum(int(c) for c in item) for item in zip(*lines)]
    if ox:
        if counts[idx] == len(lines) / 2:
            return '1'
        return '1' if counts[idx] > (len(lines) // 2 ) else '0'
    else:
        if counts[idx] == len(lines) / 2:
            return '0'
        return '0' if counts[idx] > (len(lines) // 2 ) else '1'

oxygen = lines[:]
carbon = lines[:]
for idx in range(len(lines[0])):
    if len(oxygen) != 1:
        oxygen = [line for line in oxygen if line[idx] == get_significant_bit(oxygen, idx, True)]
    if len(carbon) != 1:
        carbon = [line for line in carbon if line[idx] == get_significant_bit(carbon, idx, False)]


print(int(carbon.pop(), 2) * int(oxygen.pop(), 2))