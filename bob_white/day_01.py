data = list(map(int, open("day_01_input.txt").read().splitlines()))
print(sum(data[i + 1] > data[i] for i in range(len(data) - 1)))
windows = [sum(data[i : i + 3]) for i in range(len(data))]
print(sum(windows[i + 1] > windows[i] for i in range(len(windows) - 1)))
