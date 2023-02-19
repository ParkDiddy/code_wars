# returns multiplication table of any number
# size 3 would be [1,2,3], [2, 4, 6], [3, 6, 9] etc
def multiplication_table(size):
    size = range(1, size + 1)
    my_list = [[i * j for j in size] for i in size]
    return my_list


print(multiplication_table(3))

# test.describe("Basic Tests")
# test.it("Should pass basic tests")
# test.assert_equals(multiplication_table(3), [[1,2,3],[2,4,6],[3,6,9]])
