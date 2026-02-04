# Practice with map
# Fill out the rest of the map functions.
# You can define additional functions if you need to.
# (a) ["apple", "orange", "pear"] => (5, 6, 4)  (length)
# (b) ["apple", "orange", "pear"] => ("APPLE", "ORANGE", "PEAR")  (uppercase)
# (c) ["apple", "orange", "pear"] => ("elppa", "egnaro", "raep")  (reversed)
# (d) ["apple", "orange", "pear"] => ("ap", "or", "pe")  (first two letters)

word = ["apple", "orange", "pear"]

a = map(len, word)

# b = map(???, ???)
# c = map(???, ???)
# d = map(???, ???)
print(list(a))