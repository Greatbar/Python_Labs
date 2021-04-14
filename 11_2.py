for i in range(int(input())):
    text = str(input())
    text = []
    if '%' in text:
        print(text.replace('%', ''))
    elif text.find('####') not in text:
        print(text)
