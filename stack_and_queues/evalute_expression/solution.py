# Evalute the value fo arithmetic expression in reverse polish notation.
# ex : [2,1,+,3,*] = 9
def evalute_expression(arr):
    length = len(arr) # store the length of the array
    stack = [] # stack to store the operands
    operators = ['+','-','*','/']
    # traverse the arr
    for i in range(0,len(arr)):
        cur_ele = arr[i]
        # if the current element is operator , and we will evalute using the top two element in the stack
        if cur_ele in operators:
            value1 = stack.pop()
            value2 = stack.pop()
            value1 = int(value1)
            value2 = int(value2)
            if cur_ele == '+':
                stack.append(value1 + value2)
            elif cur_ele == '-':
                stack.append(value1 - value2)
            elif cur_ele == '*':
                stack.append(value1 * value2)
            elif cur_ele == '/':
                stack.append(value1 // value2)
        else: # if the current element is operand
            stack.append(cur_ele)
    return stack[-1]

# test case
arr = ['2','1','+','3','*']
ans = evalute_expression(arr)
print(ans)