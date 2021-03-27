# given a string , return the string in reverse order
# ex : 'abc' -> 'cba'
def revstring(string):
    stack = [] # stack to store each character of the given string
    rev_string = '' # store the string in the reverse order

    # traverse through our string
    for character in string:
        stack.append(character)
    # traverse the stack
    while len(stack) != 0: # while the stack is not empty
        cur_char = stack.pop()
        rev_string += cur_char

    return rev_string


# test case
string = 'abs'
reversed_string = revstring(string)

print(reversed_string)