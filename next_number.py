import random

# Parameters
randstart = 1
randend = 50
nums_to_make = randend - 1

raw_tbl = random.sample(range(randstart, randend), nums_to_make)

for i in raw_tbl:
    print("{}".format(i))
    input("")

