
def find_all_palindromes_list() -> list[str]:

    all_words: set[str] = get_all_words()
    pali_list: list[str] = []

    for i in all_words:

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

    return pali_list


def get_all_words() -> set[str]:
    words: list[str] = []
    with open(
        'web2.txt',
            'r', encoding='utf8') as file:
        words = [line.strip().lower()
                 for line in file if len(line) > 2]

    return set(words)
