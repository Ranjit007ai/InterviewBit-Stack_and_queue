# given a array , find the nearest smaller element for every element A[i]  in array such that element has an index smaller than i.
# if not possible smaller value , then replace -1
# A = [4,5,2,10,8] => [-1,4,-1,2,2]

def nearest_smaller_element(arr):
    stack = []
    final_output = []
    length = len(arr)
    for i in range(0,length):
        while len(stack) != 0 and arr[i] <= stack[-1]:
            stack.pop()
        if len(stack) == 0:
            final_output.append(-1)
        else:
            final_output.append(stack[-1])
        stack.append(arr[i])
    return final_output

# test case
arr = [4,5,2,10,8]
ans = nearest_smaller_element(arr)
print(ans)