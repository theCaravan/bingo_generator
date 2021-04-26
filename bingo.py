import random

# Parameters
rowlen = 5
collen = 5
randstart = 1
randend = 50
repeat = 30

nums_to_make = rowlen * collen

this_instance = 1
while this_instance <= repeat:
    raw_tbl = random.sample(range(randstart, randend), nums_to_make)

    tbl = []

    #print(raw_tbl)
    
    coli = 0
    tbl_print = ""
    for i in raw_tbl:
        if coli >= collen:
            print(tbl_print.strip())
            tbl_print = ""
            coli = 0 

        tbl_print += str(i) + " "
        coli += 1 
    print(tbl_print)

    this_instance += 1
    print("==================")
