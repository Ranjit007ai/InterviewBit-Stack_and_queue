# Given a string A denoting an expression . It contains following operator +,-,*,/
# check whether A has redudant braces or not.
# ex : A = '((a+b))' => True i.e this can be reduce to (a+b)

def braces(A):
    stack = []
    for chr in A:
        if chr == ')':
            flag = True
            top = stack[-1]
            stack.pop()
        
            while top != '(':
                if top == '+' or top =='-' or top == '*' or top == '/':
                    flag = False
                top = stack[-1]
                stack.pop()
            if flag == True:
                return True
        else:
            stack.append(chr)
    return False

# test case
A = '((a+b))' 
ans = braces(A)
print(ans)