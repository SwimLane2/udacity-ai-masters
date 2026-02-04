# Practice with map
# Fill out the rest of the map functions.
# You can define additional functions if you need to.
# (a) ["apple", "orange", "pear"] => (5, 6, 4)  (length)
# (b) ["apple", "orange", "pear"] => ("APPLE", "ORANGE", "PEAR")  (uppercase)
# (c) ["apple", "orange", "pear"] => ("elppa", "egnaro", "raep")  (reversed)
# (d) ["apple", "orange", "pear"] => ("ap", "or", "pe")  (first two letters)

word = ["apple", "orange", "pear"]

a = map(len, word)
b = map(str.upper, word)
c = map(lambda s: s[::-1], word)
d = map(lambda s: s[:2], word)
print(list(a))
print(list(b))
print(list(c))
print(list(d))