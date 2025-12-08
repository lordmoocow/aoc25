"""Advent of Code 2025 - Day 07."""

def part1(input_data: str) -> int:
    rows = input_data.strip().splitlines()
    # We start with 1 beam at the position marked "S"
    beams = set([rows[0].index("S")])
    
    # For the remaining rows of the manifold space we need to check for splitters
    # this will split into two beams. We count the number of hit a splitter.
    splits = 0
    for row in rows[1:]:
        # Collate the splitters from the current row
        splitters = [i for i, v in enumerate(row) if v == "^"]
        # Determine if these collide with the active beams
        hits = beams.intersection(splitters)
        if any(hits):
            splits += len(hits)
            
            # We need to continue to track which beams actually 
            # for upcoming manifold space

            # Retain position of beams that didn't hit anything
            beams = beams.difference(hits)
            # For those that hit, recreate them either side of the splitter
            for i in hits:
                if row[i-1] != "^":
                    beams.add(i-1)
                if row[i+1] != "^":
                    beams.add(i+1)

        # row2 = list(row)
        # for i in beams:
        #     row2[i] = "|"
        # print("".join(row2))
    return splits


