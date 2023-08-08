from aiogram.types import Message
from aiogram_dialog import DialogManager, DialogProtocol
from copy import deepcopy

tmp_database = [{"name": "Стоянка 1", "uuid": "1", "occupied": False,
                 "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."},
                {"name": "Стоянка 2", "occupied": False, "uuid": "2",
                 "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry."},
                {"name": "Стоянка 3", "occupied": True, "uuid": "3",
                 "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry."},
                {"name": "Стоянка 4", "occupied": True, "uuid": "4",
                 "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry."},
                {"name": "Стоянка 5", "uuid": "5", "occupied": False,
                 "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry."},
                {"name": "Стоянка 6", "occupied": True, "uuid": "6",
                 "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry."}]


async def getter_choice(dialog_manager: DialogManager, **kwargs):
    data = deepcopy(tmp_database)
    for item in data:
        if item["occupied"]:
            item["name"] += " 🔴"
        else:
            item["name"] += " 🟢"
    return {"camps": data}


async def getter_detail(dialog_manager: DialogManager, **kwargs):
    data = deepcopy(tmp_database)
    for item in data:
        if item["uuid"] == dialog_manager.dialog_data["camp_id"]:
            return {"data": item["description"]}
    return {"data": "Нет данных"}


async def start_camp_info(message: Message, dialog: DialogProtocol, manager: DialogManager, camp_id: int):
    manager.dialog_data["camp_id"] = camp_id
    await manager.next()
