from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Start, Url
from aiogram_dialog.widgets.text import Const, Format

from app.dialogs.states import MenuSG, InfoSG, CampSG
from app.dialogs.windows.menu.methods import getter_menu

MenuMainWin = Window(
    Format("Привет {name} {sticker}"),
    Group(
        Start(Const("Информация"), state=InfoSG.main, id="info_btn"),
        Start(Const("Стоянки"), state=CampSG.choice, id="camp_btn"),
        width=1,
    ),
    Group(
        Start(Const("Офлайн путеводитель"), state=CampSG.choice, id="pdf_btn"),
        Url(Const("Онлайн путеводитель"), Const("https://www.youtube.com/watch?v=OBg9ZAqBifQ")),
        width=2,
    ),
    getter=getter_menu,
    state=MenuSG.main,
)
