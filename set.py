# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly
# a non-negative integer n and k and returns the list that
# contains k number of subsets from the power set as sets.
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) =>
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]


# refrence from https://docs.python.org/3/library/itertools.html
import itertools


def limitedPowerSet(n, k):
    # Your code goes here...
    s = set()
    y = [{}]
    for i in range(1, n + 1):
        s.add(i)
    for i in range(1, len(s) + 1):
        z = list(map(set, itertools.combinations(s, i)))
        for j in range(len(z)):
            if(len(y) != k):
                y.append(z[j])
            else:
                return y


assert(limitedPowerSet(5, 7) == [{}, {1}, {2}, {3}, {4}, {5}, {1, 2}])
print("All test cases passed")
