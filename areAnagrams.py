# areAnagrams(s1, s2)
# Write the function areAnagrams(s1, s2) that takes two strings,
# s1 and s2, that you may assume contain only upper and/or
# lower case letters, and returns True if the strings are
# anagrams, and False otherwise. Two strings are anagrams
# if each can be reordered into the other. Treat "a" and "A"
# as the same letters (so "Aba" and "BAA" are anagrams).
# You may not use sort() or sorted() or any other list-based
# functions or approaches. Hint: you may use s.count(),
# which could be quite handy here.
# Hint: The time complexity can be achieved in Linear.

# reference from cspp
def areAnagrams(s1, s2):
    # Your code goes here...

    s1 = s1.lower()
    s2 = s2.lower()
    l1 = len(s1)
    l2 = len(s2)
    t = ""
    k = ""
    for i in s1:
        if(i in t):
            pass
        else:
            t = t+i
    for i in s2:
        if(i in t):
            pass
        else:
            k = k+i
    if(k in t):
        if(l1 == l2):
            return True
        else:
            return False
    else:
        return False


# write your test cases here...
assert(areAnagrams("ABA", "aab") == True)
assert(areAnagrams("SUMA", "amsu") == True)
assert(areAnagrams("abc", "bcd") == False)
print("All test cases passed....")
