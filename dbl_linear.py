# takes a number and adds it and 2 * x + 1 and 3 * x + 1 to the list
def dbl_linear(n):
    u = [1]
    for x in u:
        u.append(2 * x + 1)
        u.append(3 * x + 1)
        if len(u) > n * 10:
            u = set(u)  # change to set to remove duplicates
            u = list(u)  # change back to list
            u.sort()  # sort list
            return u[n]


print(dbl_linear(500))
