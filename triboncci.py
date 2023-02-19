# takes a triple fibonacci and n and gives you that amount of trib nubmers
def tribonacci(signature, n):
    if n == 0:
        return []
    if n == 1:
        return [signature[0]]
    if n == 2:
        return [signature[0], signature[1]]
    list_copy = signature.copy()
    for i in range(n - 3):
        list_copy.append(sum(list_copy[-3:]))
    return list_copy


print(tribonacci([1, 1, 1], 30))