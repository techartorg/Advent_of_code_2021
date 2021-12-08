from itertools import permutations


count = 0
for line in open("day_08_input.txt"):
    signal, output = line.strip().split("|")
    for val in output.split():
        if len(val) in (2, 7, 4, 3):
            count += 1


starter = {
    "acedgfb": 8,
    "cdfbe": 5,
    "gcdfa": 2,
    "fbcad": 3,
    "dab": 7,
    "cefabd": 9,
    "cdfgeb": 6,
    "eafb": 4,
    "cagedb": 0,
    "ab": 1,
}
# Sorting the strings so that we can compare against it later, makes it easier to match because order doesn't matter.
sorted_mapping = {"".join(sorted(k)): v for k, v in starter.items()}
count = 0
for line in open("day_08_input.txt"):
    signal, output = line.strip().split(" | ")
    # The idea here is to find a permuation where we've re-mapped a-g to another set of characters, and all of those
    # remapped strings exist in our original starter values
    for permutation in permutations("abcdefg"):
        mapping = {k: v for k, v in zip("abcdefg", permutation)}
        # Checking if all words in the signal map back to a valid known digit
        remapped = (
            "".join(sorted(mapping[c] for c in word)) in sorted_mapping
            for word in signal.split()
        )
        if all(remapped):
            # Once we've got all our values mapping back to a digit, we can go through and look them all up
            digits: list[str] = []
            for word in output.split():
                digit_code = "".join(sorted(mapping[c] for c in word))
                digits.append(str(sorted_mapping[digit_code]))

            count += int("".join(digits))
            break
print(count)
