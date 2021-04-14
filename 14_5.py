import re

test = input()
key = 'text'
print(re.search(f'\?.*?{key}=(.*)[&\n]', test)[1])
