claims = {}
overlaps = {}

with open('data.txt') as f:
    for line in f:
        i = line.index(' ')
        claim_id = int(line[1:i])
        i += 3
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

        overlaps[claim_id] = False

        for x in range(x_offset, x_offset + width):
            for y in range(y_offset, y_offset + height):
                try:
                    previous_claim_id = claims[x, y]
                except KeyError:
                    claims[x, y] = claim_id
                else:
                    overlaps[claim_id] = True
                    overlaps[previous_claim_id] = True

for claim_id, does_it_overlap in overlaps.items():
    if not does_it_overlap:
        print(claim_id)
        break