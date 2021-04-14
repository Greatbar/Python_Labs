booksInShelf = int(input('Введите сколько книг в вашей библиотеке: '))
booksForSummer = int(input('Введите сколько книг задали на лето: '))
nameBooksInShelf = []
for i in range(booksInShelf):
    nameBooksInShelf.append(input('Введите названия выших книг из библиотеки: '))
for j in range(booksForSummer):
    bookAdd = str(input('Введите названия заданных книг на лето: '))
    if bookAdd in nameBooksInShelf:
        print('YES')
    else:
        print('NO')
