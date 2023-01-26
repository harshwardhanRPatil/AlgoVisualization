n=input()
l=[]
for i in range(n):
    a,b=int(input().split())
    if a>b and (a-b)%2==0:
        l.append('1')
    elif b>a and (b-a)%2!=0:


# import re
# import sys
#
#
# def alternate(s):
#     counter = 0
#     d = {}
#     cheack_list = {}
#
#     length = len(s)
#     if length < 3:
#         return length
#     for i in range(length - 2):
#
#         if s[i] in cheack_list:
#             pass
#         else:
#             cheack_list[s[i]] = 1
#             step = 1
#             j = i + 1
#             val = 1
#             ban = {}
#             up = 0
#             flag = True
#             while j < length:
#
#                 if s[j] == s[i]:
#                     val += 1
#                     step += 1
#                     j += 1
#                     print(s[i])
#                     print(up)
#                     print(step)
#                     print(d)
#
#                     if up > 0:
#                         up = 0
#
#                     else:
#                         flag = False
#                         break
#
#                 elif s[j] in d:
#                     d[s[j]] += 1
#                     if d[s[j]] > step:
#                         ban[s[j]] = 1
#                         d.pop(s[j])
#                         # if len(d)==0:
#                         up -= 1
#                     else:
#                         up += 1
#
#                 elif step == 1 and s[j] not in ban:
#                     d[s[j]] = 1
#                     up += 1
#
#                 j += 1
#
#             # print(d)
#             # print(step)
#             # print(flag)
#             # print(val)
#             if flag == False or len(d) == 0:
#
#                 pass
#             else:
#                 # print(s[i])
#                 Keymax = max(d, key=lambda x: d[x])
#                 counter = max(counter, val + d[Keymax])
#
#             d.clear()
#         # for i in d:
#     return counter
#
#
# if __name__ == '__main__':
#     result = alternate("asvkugfiugsalddlasguifgukvsa")
#     print(result)
#
#
#
#
