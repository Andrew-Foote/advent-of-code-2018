with open('data.txt') as f:
    print(sum(int(line) for line in f))