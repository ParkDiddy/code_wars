def move_zeros(lst):
    zeros = []
    for i in range(len(lst)-1, -1, -1):
        if lst[i] == 0:
            zeros.append(lst.pop(i))
    lst.extend(zeros)
    return lst



print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))