# Дан список
first = (1, (2, (3, (4, None))))
prev = None
node = first
while node != None:
    next = node[1]
    node[1] = prev
    prev = node
    node = next