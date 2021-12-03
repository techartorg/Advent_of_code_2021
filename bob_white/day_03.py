

lines = [line.strip() for line in open('day_03_input.txt')]
counts = [sum(int(c) for c in item) for item in zip(*lines)]
gamma_str = ''.join('1' if c > len(lines)/2 else '0' for c in counts)
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
for idx in range(len(lines[0])):
    if len(oxygen) == 1:
        break
    oxygen = [line for line in oxygen if line[idx] == get_significant_bit(oxygen, idx, True)]
print(oxygen)
carbon = lines[:]
for idx in range(len(lines[0])):
    if len(carbon) == 1:
        break
    carbon = [line for line in carbon if line[idx] == get_significant_bit(carbon, idx, False)]
print(carbon)
print(int(carbon[0], 2) * int(oxygen[0], 2))