ingredients = set()
ingredient_eat = set()
ingredients_fridge = int(input('Число продуктов в холодильнике: '))
for i in range(ingredients_fridge):
    ingredients.add(input())

recipe_name_count = int(input())
for i in range(recipe_name_count):
    recipe_name = input()
    ingredient_eat_M = int(input())
    do = True
    for j in range(ingredient_eat_M):
        ingredient_eat.add(input())
    for k in ingredient_eat:
        if not k in ingredients:
            do = False
    if do:
        print(recipe_name)
    ingredient_eat = set()
