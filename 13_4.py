number = int(input())
first = [int(input()) for i in range(number)]
second = first[:]
training = int(input())
for i in range(training):
    brother = int(input())
    if brother == 1:
        first[int(input())] += int(input())
    elif brother == 2:
        second[int(input())] += int(input())
print(*first)
print(*second)
result = 0
for i in range(len(first)):
    if first[i] == second[i]:
        result = result + 1
print(result)
