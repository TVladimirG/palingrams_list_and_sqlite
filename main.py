import time

# from find_palindromes_sqlite import find_all_palindromes_sqlite
from find_palindromes_list import find_all_palindromes_list


def main() -> None:

    # print('Ищем палиндромы с помощью базы на sqlite')
    # print(f'Начало поиска {datetime.datetime.now()}')

    # pali_list: list[str] = find_all_palindromes_sqlite()

    # print(f'Всего палиндромов {len(pali_list)}')
    # print(f'Конец поиска {datetime.datetime.now()}')

    # ********************************************************
    # Разница в скорости поиска между sqlite и list - ожидаемо
    #   в несколько раз (разумеется в пользу list)
    # А если вместо list использовать set то еще в несколько тысяч раз быстрее
    # в итоге программа работает всего ~0.902 сек


    print('Ищем палиндромы с помощью обычного списка')

    start = time.time()
    pali_list: list[str] = find_all_palindromes_list()
    end = time.time()

    print(f'Всего палиндромов {len(pali_list)}')
    delta = end-start
    print(f'Время поиска {delta:.3f} сек')


main()
