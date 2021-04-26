import random

# Parameters
rowlen = 5
collen = 5
randstart = 1
randend = 50
repeat = 10

nums_to_make = rowlen * collen

this_instance = 1
while this_instance <= repeat:
    raw_tbl = random.sample(range(randstart, randend), nums_to_make)

    tbl = []



    print(raw_tbl)

    this_instance += 1
