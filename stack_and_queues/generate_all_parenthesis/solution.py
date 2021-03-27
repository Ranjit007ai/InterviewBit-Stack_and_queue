# Given a string containing only (,),{,},[,]
# determine if input string is valid or not 

def isvalid_parenthesis(string):
    stack = [] # stack to store the brackets
    opening_brackets = ['[','{','(']
    # traverse the string
    for bracket in string:
        # if the current bracket is opening bracket , then push it into the stack
        if bracket in opening_brackets:
            stack.append(bracket)
        else: # if it is the close bracket
            # if the stack is empty , means there is no opening bracket before this closing bracket i.e. invalid string
            if len(stack) == 0:
                return False 
            top_element = stack.pop()
            if top_element == '[' and bracket == ']': 
                continue
            elif top_element == '(' and bracket == ')':
                continue
            elif top_element == '{' and bracket == '}':
                continue
            else:
                return False
    return True

# test case
string = '[[]]}'
ans = isvalid_parenthesis(string)
print(ans)