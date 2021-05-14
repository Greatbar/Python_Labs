import collections

d = collections.defaultdict(list)
n = int(input())
for _ in range(n):
    e = input()
    d[tuple(sorted(list(e.lower())))].append(e.lower())
v = d.values()
v = filter(lambda w: len(set(w)) > 1, v)
ans = map(lambda x: ' '.join(sorted(x)), v)
print('\n'.join(sorted(ans)))
