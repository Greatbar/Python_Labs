meals = [input() for i in range(int(input()))]
meals_served = []
for i in range(int(input())):
    meals_served += [input() for k in range(int(input()))]
for i in sorted(meals):
    if i not in meals_served:
        print(i)
