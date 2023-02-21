#  Traverse a binary tree and find the node that is incorrect.
def find_incorrect_value(tree):
    def parent_index(current_index):
        return 0 if current_index == 0 else -(current_index // 2 + 1)

    for index, node in enumerate(tree):
        left = (2 * index) + 1
        right = (2 * index) + 2
        child_index = index * 4
        if node != tree[left] + tree[right]:
            if index * 4 + 4 > len(tree):
                return right, node - tree[left]
            if tree[left] != tree[child_index + 3] + tree[child_index + 4]:
                if tree[index + parent_index(index)] == node + tree[index - 1 if index % 2 == 0 else index + 1]:
                    return left, node - tree[right]
                return left, tree[left + 2] + tree[left + 3]
            if tree[right] != tree[child_index + 5] + tree[child_index + 6]:
                return right, node - tree[left]
            return tree.index(node), tree[left] + tree[right]


print(find_incorrect_value([28, 13, 14, 6, 7, 5, 9]))  # should return 0, 27
print(find_incorrect_value([27, 14, 14, 6, 7, 5, 9]))  # should return 1, 13
print(find_incorrect_value([19, 9, 10, 5, 5, 4, 6, 2, 2, 1, 4, 1, 3, 2, 4]))  # should return 3, 4
print(find_incorrect_value([29, 13, 16, 5, 8, 9, 1]))  # should return 6, 7
print(find_incorrect_value([29, 13, 16, 5, 7, 9, 7]))  # should return 4, 8
print(find_incorrect_value([5, 2, 2, 1, 1, 2, 1]))  # should return 2, 3
print(find_incorrect_value([19, 9, 10, 4, 5, 4, 6, 3, 2, 1, 4, 1, 3, 2, 4]))  # should return 8, 1
print(find_incorrect_value([9, 5, 4, 2, 3, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1]))  # should return 5, 2
print(find_incorrect_value([9, 5, 4, 2, 3, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1]))  # should return 6, 2
