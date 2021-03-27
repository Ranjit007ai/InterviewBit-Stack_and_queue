# given a string A representing an absolutte path for file ,return the string A after simplifying absolute path.
#note: Absolute path always begin with % (root dictory)
#ex input: A= '/a/./b/../../c/' => o/p: '/c'

def simplify_path(A):
    stack1 , stack2 = [] , []
    res = '/'
    index = 0
    length = len(A)
    while index < length:
        sub_string = ''
        while index < length and A[index] == '/':
            index += 1
        while index < length and A[index] != '/':
            sub_string += A[index]
            index += 1
        if sub_string == '..':
            if stack1:
                stack1.pop()
        elif sub_string == '.':
            continue
        elif len(sub_string) > 0:
            stack1.append(sub_string)
        index += 1
    while stack1:
        ele = stack1.pop()
        stack2.append(ele)
    while stack2:
        if len(stack2) == 1:
            res += stack2[-1]
        else:
            res += stack2[-1] + '/'
        stack2.pop()
    return res

        
# test case
A  = '/a/b/./../../c/'
ans = simplify_path(A)
print(ans)