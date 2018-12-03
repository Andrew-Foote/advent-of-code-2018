claims = {}
double_claim_count = 0

with open('data.txt') as f:
    for line in f:
        i = line.index('@') + 2
        j = line.index(',', i)
        x_offset = int(line[i:j])
        i = j + 1
        j = line.index(':', j)
        y_offset = int(line[i:j])
        i = j + 2
        j = line.index('x', i)
        width = int(line[i:j])
        i = j + 1
        height = int(line[i:])

        for x in range(x_offset, x_offset + width):
            for y in range(y_offset, y_offset + height):
                try:
                    claimed_exactly_once = claims[x, y] == 1
                except KeyError:
                    claims[x, y] = 1
                else:
                    if claimed_exactly_once:
                        claims[x, y] = 2
                        double_claim_count += 1

print(double_claim_count)