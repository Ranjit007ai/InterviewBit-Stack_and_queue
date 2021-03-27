# given a integer array A of non-negative integers representing an elevation map where width of each bar is 1, compute how much water able to 
# trap after raining.
def trap(A):
    stack = []
    ans = 0
    for i in range(len(A)):
        while stack and A[stack[-1]] < A[i]:
            pop_height = A[stack[-1]]
            stack.pop()
            if not stack :
                break
            distance = i - stack[-1] - 1
            min_height = min(A[stack[-1]],A[i]) - pop_height
            ans += distance * min_height
        stack.append(i)
    return ans

# test case
A = [0,1,0,2,1,0,1,3,2,1,2,1]
ans = trap(A)
print(ans)