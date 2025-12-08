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


def part2(input_data: str) -> int:
    rows = input_data.strip().splitlines()
    max_x = len(rows[0])
    beam = rows[0].index("S")

    # At the manifold exit we know there are no additional possible timelines
    # And because I know that each splitter immediately before that introduces
    # 2 possible timelines, and each previous split also introduced 2 timelines.
    # So in theory, if I work from the exit I know exactly how many possible timelines
    # that I've come accross, I can accumulate these timelines as I travel back in time
    # and determine the total number of possible timelines for any given entry point.

    # We know there is always at least 1 timeline that will exit the manifold
    timeline: list[int] = [1] * max_x

    rows.reverse()
    for row in rows[:-1]:
        # Collate splitters in current manifold space
        splitters = [i for i, v in enumerate(row) if v == "^"]
        for splitter in splitters:
            # Because this is travelling in reverse, we essentially need to recombine
            # the beams to trace their timelines.
            # The accumulated timeline of each beam is therefore combined into the
            # manifold space where it would originally have split.
            timeline[splitter] = timeline[splitter-1] + timeline[splitter+1]
            
    # the tachyon entry point determines possible timelines it will create
    return timeline[beam]
