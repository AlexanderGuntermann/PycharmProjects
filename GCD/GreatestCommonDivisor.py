def findGCD(a,b):
    if b == 0:
        return a

    else:

        return (findGCD(b, a%b))


print(findGCD(100,24))

print(findGCD(200,100))


# def findExtendedGCD(a,b):
#     x = 0
#     y = 1
#     u = 1
#     v = 0
#     while a != 0:
#         q = b // x
#         r = b % a
#         m = x - u * q
#         n = y - v * q
#         b = a
#         a = r
#         x = u
#         y = v
#         u = m
#         v = n
#     gcd = b
#     return gcd, x, y
#
#
# print(findExtendedGCD(100,24))

