number = input()
print(*[i for i in input().split() if number.upper() in i or number in i],sep='\n')