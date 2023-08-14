from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Start, Url
from aiogram_dialog.widgets.text import Const, Format

from app.dialogs.states import MenuSG, InfoSG, CampSG
from app.dialogs.windows.menu.methods import getter_menu

MenuMainWin = Window(
    Format("Привет {name}!"),
    Group(
        Start(Const("🏛 История"), state=InfoSG.main, id="info_btn"),
        Start(Const("⛺️ Стоянки"), state=CampSG.choice, id="camp_btn"),
        width=1,
    ),
    Group(
        Url(Const("🗺 Онлайн путеводитель"), Const("https://map.gortem.ru/")),
        width=2,
    ),
    getter=getter_menu,
    state=MenuSG.main,
)
