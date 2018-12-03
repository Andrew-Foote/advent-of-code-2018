from collections import Counter

double_count = 0
triple_count = 0

with open('data.txt') as f:
    for line in f:
        counter = Counter()
        
        for c in line[:-1]:
            counter[c] += 1

        has_double = False
        has_triple = False

        for letter, count in counter.items():
            if count == 2:
                has_double = True
            elif count == 3:
                has_triple = True

        double_count += has_double
        triple_count += has_triple

print(double_count * triple_count)