# LINK: https://www.hackerrank.com/challenges/apple-and-orange/problem

# starting point of Sam's house location.
s = 7

# ending location of Sam's house location.
t = 11

# location of the Apple tree.
a = 5

# location of the Orange tree.
b = 15

# distance at which each apple falls from the tree.
apples_distances = [-2, 2, 1]

# distance at which each orange falls from the tree.
oranges_distances = [5, -6]


def countApplesAndOranges(s, t, a, b, apples, oranges):

    apples_result = sum([1 for distance in apples if (
        distance + a) >= s and (distance + a) <= t])

    oranges_result = sum([1 for distance in oranges if (
        distance + b) >= s and (distance + b) <= t])

    print(apples_result)
    print(oranges_result)


countApplesAndOranges(s, t, a, b, apples_distances, oranges_distances)
