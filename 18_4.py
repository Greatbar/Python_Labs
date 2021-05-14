def bracket_check(string):
    stack = list()
    for element in string:
        if element == "(":
            stack.append(element)
        elif element == ")":
            stack.pop()
    print(('NO', 'YES')[len(stack) == 0])
