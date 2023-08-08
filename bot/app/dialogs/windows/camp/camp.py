from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Start, Url, ScrollingGroup, Select, Cancel, Back
from aiogram_dialog.widgets.text import Const, Format

from app.dialogs.states import CampSG
from app.dialogs.windows.camp.methods import getter_choice, start_camp_info, getter_detail

CampChoiceWin = Window(
    Const("Выберите стоянку:"),
    Group(
        ScrollingGroup(
            Select(Format("{item[name]}"), "camp_btn", lambda camp: camp["id"], "camps",
                   on_click=start_camp_info),
            width=3, height=5,
            id="camps_group"),
        Cancel(Const("Меню")),
    ),
    state=CampSG.choice,
    getter=getter_choice,
)

CampDerailedWin = Window(
    Format("Информация о стоянке:\n\n{data}"),
    Back(Const("Назад")),
    state=CampSG.main,
    getter=getter_detail,
)