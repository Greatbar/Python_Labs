string = input().upper()
k = 0
for i in range(len(string)):
    if string.count(string[i]) > k:
        k = string.count(string[i])
print(k)
