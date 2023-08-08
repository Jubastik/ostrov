from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Cancel
from aiogram_dialog.widgets.text import Const

from app.dialogs.states import InfoSG

_text = "Ки́льпола — остров в Ладожском озере. Является западной оконечностью Ладожских шхер. Расположен в северо-западной части озера. На западе связан мостом с материком. Находится на территории Хийтольского сельского поселения в Лахденпохском районе Карелии, в трёх километрах от границы с Ленинградской областью."

InfoMainWin = Window(
    Const(_text),
    Group(Cancel(Const("Назад")),
          ),
    state=InfoSG.main,
)
