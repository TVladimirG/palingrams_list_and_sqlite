import datetime

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

    print('Ищем палиндромы с помощью обычного списка')

    print(f'Начало поиска {datetime.datetime.now()}')
    pali_list: list[str] = find_all_palindromes_list()

    print(f'Всего палиндромов {len(pali_list)}')
    print(f'Конец поиска {datetime.datetime.now()}')


main()
