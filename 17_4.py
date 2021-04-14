records_count = int(input())
records = input()
time = 0
public, likes = records.split(' опубликовал пост, количество просмотров: ')
access = {public: [int(likes), 'root', time]}
for i in range(1, records_count):
    records = input()
    time += 1
    if ' отрепостил пост у ' in records:
        repost, records = records.split(' отрепостил пост у ')

        if ', количество просмотров: ' in records:
            author, likes = records.split(', количество просмотров: ')
            likes = int(likes)
            access[repost] = [likes, author, time]
            while author != 'root':
                access[author][0] += likes
                author = access[author][1]
    elif 'количество просмотров: ' in records:
        records, likes = records.split('количество просмотров: ')
        access[public][0] += int(likes)
for x in sorted(access, key=lambda y: access[y][2]):
    print(access[x][0])
