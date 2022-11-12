
def find_all_palindromes_list() -> list[str]:

    all_words: list[str] = get_all_words()
    pali_list: list[str] = []

    itr: int = 0

    for i in all_words:
        # Найти первые ХХХ и остановиться
        # if len(pali_list) >= 250:
        #     return pali_list

        # выводить каждые 1000 элементов
        itr += 1
        if itr % 1000 == 0:
            print(iter)

        word: str = i
        len_word: int = len(word)
        if len_word > 1:
            for i in range(0, len_word):

                # Отнимаем буквы с конца слова
                l_side: str = word[:len(word)-i:]
                r_side: str = word[len(word)-i::]

                # Проверяем если правая сторона = палиндром
                if r_side == r_side[::-1]:

                    # И левая сторона развернутая наоборот есть в базе данных
                    # Тогда это палиндромная фраза!
                    search_word: str = l_side[::-1]
                    if search_word in all_words:
                        pali_list.append(search_word)
                        # print(f'{word} {search_word}')

                 # Отнимаем буквы с начала слова
                l_side: str = word[:i:]
                r_side: str = word[i::]

                # Проверяем если левая сторона = палиндром
                if l_side == l_side[::-1]:

                    # И правая сторона развернутая наоборот есть в базе данных
                    #  Тогда это палиндромная фраза!
                    search_word: str = r_side[::-1]
                    if search_word in all_words:
                        pali_list.append(search_word)
                        # print(f'{search_word} {word}')

    return pali_list


def get_all_words() -> list[str]:
    words: list[str] = []
    with open(
        'web2.txt',
            'r', encoding='utf8') as file:
        words = [line.strip().lower()
                 for line in file if len(line) > 2]

        #  Далее пробежимся по нему, и добавим каждое слово в таблицу
    # for word in words:
    #     __l.append(word)
    return words
