def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*(n[i] for i in range(0, 10)))

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))