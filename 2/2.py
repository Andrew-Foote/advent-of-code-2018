import string
import sys

identifiers = set()

with open('data.txt') as f:
    for line in f:
        identifier = line[:-1]
        for i, c in enumerate(identifier):
            for substitution in string.ascii_lowercase:
                if (
                    substitution != c and
                    identifier[:i] + substitution + identifier[i + 1:] in identifiers
                ):
                    print(identifier[:i] + identifier[i + 1:])
                    sys.exit()

        identifiers.add(identifier)