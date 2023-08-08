from aiogram.types import Message
from aiogram_dialog import DialogManager, DialogProtocol
from copy import deepcopy

tmp_database = [{"id": 1,
                 "name": "Мятный берег",
                 "visibility": "Хорошая, широкая",
                 "ashore": "Каменистый, низкий, удобный",
                 "number_tents": 2,
                 "firewood": None,
                 "conveniences": "Хорошо сложенный очаг",
                 "connection": "Yota, Megafon - 1/4, Е",
                 "mosquitoes": "Непродуваемое место",
                 "attractions": "Мята, черника, грибы",
                 "size": "Маленькая площадь",
                 "view": "Вид на закат",
                 "occupied": False,
                 },
                {"id": 2,
                 "name": "Обзорная",
                 "visibility": "Только с короткой дистанции",
                 "ashore": "Щебень и крупные камни, низкий ",
                 "number_tents": 5,
                 "firewood": None,
                 "conveniences": "Тумбочка, верёвка для сушки белья, большой очаг",
                 "connection": "МТС - 4/4, Yota, Megafon - 2/4 LTЕ/Е",
                 "mosquitoes": "Продуваемое место",
                 "attractions": "Брусника",
                 "size": "Длинная и протяженная",
                 "view": "Вид на рассвет",
                 "occupied": True,
                 },
                {"id": 3,
                 "name": "Шашлычники",
                 "visibility": "Отличная",
                 "ashore": "Песчано-каменистый, низкий",
                 "number_tents": 2,
                 "firewood": True,
                 "conveniences": "Стол, хорошо сложенный очаг",
                 "connection": "Отсутствует",
                 "mosquitoes": "Непродуваемое место",
                 "attractions": "Черника, земляника, грибы",
                 "size": "Маленькая площадь среди деревьев и скал",
                 "view": "Вид на рассвет",
                 "occupied": False,
                 },
                {"id": 4,
                 "name": "Кристальная",
                 "visibility": "Плохая",
                 "ashore": "Каменистый, низкий, деревья",
                 "number_tents": 2,
                 "firewood": True,
                 "conveniences": "Хорошо сложенный очаг",
                 "connection": "Отсутствует",
                 "mosquitoes": "Непродуваемое место",
                 "attractions": "Брусника, черника, грибы",
                 "size": "Маленькая площадь среди деревьев",
                 "view": "Отсутствует",
                 "occupied": None,
                 },
                {"id": 5,
                 "name": "Колыбельный мыс",
                 "visibility": "Хорошая",
                 "ashore": "Скалистый, высокий",
                 "number_tents": 4,
                 "firewood": True,
                 "conveniences": "Хорошо сложенный очаг",
                 "connection": "МТС",
                 "mosquitoes": "Продуваемое место",
                 "attractions": "Брусника, черника, грибы",
                 "size": "Средняя площадь на скалах",
                 "view": "Вид на рассвет",
                 "occupied": None,
                 },
                ]


def text_occupied(occupied):
    if occupied is None:
        return "Занятость неизвестна"
    elif occupied:
        return "Занято"
    else:
        return "Свободно"


async def getter_choice(dialog_manager: DialogManager, **kwargs):
    data = deepcopy(tmp_database)
    for item in data:
        if item["occupied"] is None:
            item["name"] += " ⚪️"
        elif item["occupied"]:
            item["name"] += " 🔴"
        else:
            item["name"] += " 🟢"
    return {"camps": data}


async def getter_detail(dialog_manager: DialogManager, **kwargs):
    data = deepcopy(tmp_database)
    for item in data:
        if item["id"] == dialog_manager.dialog_data["camp_id"]:
            return {"data": f'📝 Название {item["name"]}\n'
                            f'○ Занятость: {text_occupied(item["occupied"])}\n'
                            f'○ Видимость с воды: {item["visibility"]}\n'
                            f'○ Берег: {item["ashore"]}\n'
                            f'○ Количество палаток: {item["number_tents"]}\n'
                            f'○ Дрова: {"Есть" if item["firewood"] else "Нет"}\n'
                            f'○ Удобства: {item["conveniences"]}\n'
                            f'○ Связь: {item["connection"]}\n'
                            f'○ Комары: {item["mosquitoes"]}\n'
                            f'○ Достопримечательности: {item["attractions"]}\n'
                            f'○ Размер: {item["size"]}\n'
                            f'○ Вид: {item["view"]}'
                    }
    return {"data": "Нет данных"}


async def start_camp_info(message: Message, dialog: DialogProtocol, manager: DialogManager, camp_id: int):
    manager.dialog_data["camp_id"] = int(camp_id)
    await manager.next()
