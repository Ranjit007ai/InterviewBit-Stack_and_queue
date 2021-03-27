# given an array , the special product of each element is defined as the product of following:
# leftspecial value: for index i, it is defined as index j such that A[j] > A[i] and i > j .If multiple A[j] then choose j nearest to i (max j )
# right pecial value: for index i, it is defined as index j such that A[j] > A[i] and j > i .If multiple A[j] then choose j nearest to i (min j )

def left_largest(arr):
    left_list = [0] * len(arr)
    stack = []
    for i in range(0,len(arr)):
        while len(stack) != 0 and arr[i] >= arr[stack[-1]]:
            stack.pop()
        if len(stack) != 0:
            left_list[i] = stack[-1]
        else:
            left_list[i] = 0
        stack.append(i)
    return left_list

def right_largest(arr):
    right_list = [0] * len(arr)
    stack = []
    for i in range(len(arr)-1,-1,-1):
        while len(stack) != 0 and arr[i] >= arr[stack[-1]]:
            stack.pop()
        if len(stack) != 0:
            right_list[i] = stack[-1]
        else:
            right_list[i] = 0
        stack.append(i)
    return right_list

def max_product(arr):
    left_list = left_largest(arr)
    right_list = right_largest(arr)
    ans = 0
    # we are not including the first and last index since , left_special for first index and right_special for lastindex will be zero.product will be zero.

    for i in range(1,len(arr)-1):
        if left_list[i] == 0 or right_list[i] == 0:
            ans = max(ans,0)
        else:
            temp = (left_list[i]) * (right_list[i])
            ans = max(ans,temp)
    return ans % ( 1000000000 + 7 )


# test case
arr = [1,4,3,4]
ans = max_product(arr)
print(ans)