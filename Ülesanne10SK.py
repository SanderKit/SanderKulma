import re

f = open("lorem.txt")
r = f.readlines()
for i in range(len(r)):
    if re.search('^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$', r[i]):
        print(r[i], end="")

