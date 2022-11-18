from db import DataBase


def find_all_palindromes_sqlite() -> list[str]:

    data_base: DataBase = DataBase()
    data_base.initial_db()

    all_words: set[str] = data_base.all_words()
    pali_list: list[str] = []

    for i in all_words:
        # if len(pali_list) >= 150:
        #     return pali_list

        word: str = i[0]
        len_word: int = len(word)
        if len_word > 1:
            for i in range(0, len_word):
                # Отнимаем буквы справа от слова

                l_side: str = word[:len(word)-i:]
                r_side: str = word[len(word)-i::]
                # Проверяем что r_side = палиндром
                # И палиндром l_side есть в базе данных
                #  Тогда это палиндромная фраза!
                if r_side == r_side[::-1]:
                    found_word: str | None = data_base.find_word(l_side[::-1])
                    if found_word is not None:
                        #  Тогда это палиндромная фраза!
                        pali_list.append(found_word)
                        # print(f'{word} {found_word}')

                # Отнимаем буквы слева от слова
                l_side: str = word[:i:]
                r_side: str = word[i::]
                # Проверяем что l_side = палиндром
                # И палиндром r_side есть в базе данных
                #  Тогда это палиндромная фраза!
                if l_side == l_side[::-1]:
                    found_word: str | None = data_base.find_word(
                        r_side[::-1])
                    if found_word is not None:
                        #  Тогда это палиндромная фраза!
                        pali_list.append(found_word)
                        # print(f'{found_word} {word}')

    return pali_list
