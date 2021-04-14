buys = []
buy_list = []
for i in range(int(input())):
    buys.append(input())
    buy_list.append(int(input()))
for i in range(len(buy_list)):
    print(buys[len(buys) - 1 - i], buy_list[len(buy_list) - 1 - i])
