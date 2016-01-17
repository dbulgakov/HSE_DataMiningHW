# d - dict
d = dict()
reverse_d = dict()

for i in d.keys():
    if d[i] in reverse_d:
        reverse_d[d[i]].add(i)
    else:
        reverse_d[d[i]] = [i]