# finds the int that appears an odd number of times
def find_it(seq):
    for x in seq:
        if seq.count(x) <= 1 or seq.count(x) % 2 != 0:
            return seq[seq.index(x)]


print(find_it([1, 10, 10, 10]))
