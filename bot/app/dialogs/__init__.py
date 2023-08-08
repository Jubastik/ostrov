from aiogram import Dispatcher

from app.dialogs.dialogs import MenuDLG, InfoDLG, CampDLG


def register_dialogs(dp: Dispatcher):
    dp.include_router(MenuDLG)
    dp.include_router(InfoDLG)
    dp.include_router(CampDLG)
