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

    field_ = init_field(3, '| |')
    for a in field_:
        print('_'*21)
        print(a)
    print('_' * 21)

