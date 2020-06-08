def reverse_a(some_str):
    '''
    The function reverses a string, reverse_a("string")
    '''
    list_a = []
    for char in some_str:
        list_a.insert(0, char)
    print("".join(list_a))


def reverse_b(some_str):
    '''
    The function reverses a string, reverse_b("string")
    '''
    lc = []
    [lc.insert(0, char) for char in some_str]
    print("".join(lc))