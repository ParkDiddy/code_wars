def count_inversions(array):
    inversion_count = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                inversion_count += 1
    return inversion_count


print(count_inversions([6, 5, 4, 3, 3, 3, 3, 2, 1]))
