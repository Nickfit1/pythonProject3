from typing import Union, Optional

EMPTY_CELL = " "


def init_field(size: int, empty_cell: str = EMPTY_CELL) -> list[list]:
    """
    Создаёт и возвращет пустое поле для игры

    :param size: размер поля
    :param empty_cell: чем заполняется пустая ячейка
    :return: отображение пустого поля в виде листа листов

    """
    # TODO Можно выбрать своё представление поля, допустим строковое или одномерный список
    return [[empty_cell] * size for _ in range(size)]


def draw_field(field):
    """
    Функция рисует поле
    :param field: Объект поля
    :return: None
    """
    pass  # TODO Написать реализацию


def get_int_val(text: str, border: tuple[int, int] = None) -> int:
    """
    Проверяет и возвращает число (это может быть необходимо когда вы хотите проверить,
        что пользователь ввел именно число и это число лежит в диапазоне border[0] и border[1]).
        Спрашиваем у пользователя ввод числа с текстом text и проверяем что оно соответствует требованиям, если не
        соответствует хотя бы одному требованию, то заново просим ввести число.

    :param text: Текст перед получением числа
    :param border: Ограничение на число (минимум, максимум)
    :return: Возвращает число, которое ввёл пользователь и прошедшее все проверки
    """
    # TODO Написать реализацию

    return


def get_char_val(text: str, req_list: list) -> str:
    """
    Проверяет и возвращает строку из необходимого списка элеменов (req_list).
    Спрашиваем у пользователя ввод строку с текстом text и проверяем что оно соответствует требованиям, если не
        соответствует хотя бы одному требованию, то заново просим ввести строку.

    :param text: Текст перед получением числа
    :param req_list: Ограничение на число
    :return: Строка
    """
    # TODO Написать реализацию

    return


def get_index_from_table(field, size: int):
    """
    Получаем индексы куда можем поставить символ игрока.
    Спрашиваем у пользователя куда он хочет поставить, проверяем свободна ли ячейка, если занята,
        то просим заново выбрать куда поставить
    :param field:
    :param size:
    :return: Возвращаем индекс ячейки куда поставил пользователь
    """

    # TODO Написать реализацию

    return


def set_player_in_field(field,
                        current_player: str,
                        index_step):
    """
    Ставим игрока на поле. По переданным координатам index_step ставим игрока current_player на поле field
    :param field:
    :param current_player:

    :return: Возвращаем поле с текущим ходом игрока
    """

    # TODO Написать реализацию

    return


def is_win(field) -> bool:
    """
    Определяем произошла ли победа. Если на текущем поле выигрышная комбинация, то возвращает True. Если никто не выиграл,
        то возвращаем False
    :param field:
    :return: bool
    """

    # TODO Написать реализацию

    return


def change_player(current_player: str) -> str:
    """
    Определяет кто ходит следующий

    :param current_player: Текущий игрок
    :return:
    """

    # TODO Написать реализацию

    return


def game(player: str, size: int) -> Optional[str]:
    """
    Запускает игру

    :param player: игрок которых ходит первым
    :param size: размер поля
    :return: возвращаем None если ничья или возвращаем игрока кто победил
    """

    # TODO Написать реализацию

    """
    В работе использовать функции написанные выше

    Возможный алгоритм работы функции:

    Инициализируем поле для игры с заданным размером
    Отрисовываем текущее поле
    Инициализируем счетчик ходов
    Запускаем цикл while с условием пока счетчик меньше числа возможных ходов
        Получаем индексы куда поставил игрок (с проверками)
        Обновляем поле по тем индексам
        Отрисовываем поле
        Увеличиваем счётчик ходов
        Проводим проверку кто выиграл, если кто-то выиграл то возвращаем кто выиграл
        Меняем игрока на следующего
    Если шаги закончились, а никто не выиграл, значит у нас ничья!
    """


def app():
    """
    Запуск приложения игры крестики-нолики
    :return:
    """

    """
    В работе использовать функции написанные выше

    Здесь можете спросить у пользователя на каком полу он хочет играть
    Кто будет ходить первым, может это будет X, а может 0
    С кем будет играть пользователь, с другим человеком или с компьютером. Если с человеком, то запустите ему игру,
        если выберет с компьютером, то напишите, что пока это в разработке.
    """

    # TODO Написать реализацию


if __name__ == "__main__":
    app()