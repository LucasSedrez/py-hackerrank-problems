# Lily has a chocolate bar that she wants to share it with Ron for his birthday.
# Each of the squares has an integer on it. She decides to share a contiguous segment of the bar selected
# such that the length of the segment mathches Ron's birth month and the sum of the integers on
# the squares is equal to his birth day. You must determine how many ways she can divide the chocolate.

n = 5  # number of squares in the chocolate bar
s = [1, 2, 1, 3, 2]  # the numbers on the chocolate squares
d = 3  # birth day
m = 2  # birth month


def solve(n, s, d, m):
    return sum([1 for x in range(0, n) if sum(s[x:x+m]) == d])


result = solve(n, s, d, m)
print(result)
