# t=int(input())
#
# container=[]
#
# for x in range(t):
#
#     n=int(input())
#     tm=(n*(n-1))//2-1
#     # print(tm)
#     array=list(map(int,input().split()))
#     start=0
#     for i in range(len(array)):
#         for j in range(0, len(array) - i - 1):
#
#             # To sort in descending order, change > to < in this line.
#             if array[j] > array[j + 1]:
#                 # swap if greater is at the rear position
#                 (array[j], array[j + 1]) = (array[j + 1], array[j])
#                 start+=1
#                 if start>tm:
#                     container.append('NO')
#                     break
#     if start<=tm:
#         container.append('YES')
#
# print("\n".join(container))
def run(h):
    stack = []
    area = 0
    i = 0
    while i < len(h):

        if not stack or h[stack[-1]] <= h[i]:
            stack.append(i)
            i += 1

        else:
            top = stack.pop()
            area = max(area, h[top] * (i - stack[-1] - 1 if stack else i))
        print(stack)
    while stack:
        top = stack.pop()
        area = max(area, h[top] * (i - stack[-1] - 1 if stack else i))

    return area
h=[1,2,3,4,5,1,5,5,5,5,5,5,5]
print(run(h))