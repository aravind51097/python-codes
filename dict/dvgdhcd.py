from collections import Counter as c

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d=c(d1)+c(d2)
print(d)
