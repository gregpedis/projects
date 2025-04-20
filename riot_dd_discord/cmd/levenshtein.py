
def get_distance(fst, snd):
    fst_size = len(fst)
    snd_size = len(snd)
    # add 1 because of the 0 column/row on d.
    d = [[0 for i in range(snd_size+1)]
        for j in range(fst_size+1)]

    for i in range(fst_size+1):
        d[i][0] = i

    for j in range(snd_size+1):
        d[0][j] = j

    # add 1 because range is right-exclusive.
    positions = [(x, y)
                 for x in range(1, fst_size+1)
                 for y in range(1, snd_size+1)]

    for i, j in positions:
        # subtract one from weight
        # cause array i 1-based but input is 0-based.
        sub_weight = 0 if fst[i-1] == snd[j-1] else 1

        sub_cost = d[i-1][j-1] + sub_weight
        del_cost = d[i-1][j] + 1
        ins_cost = d[i][j-1] + 1
        d[i][j] = min(sub_cost, del_cost, ins_cost)

    return d[fst_size][snd_size]
