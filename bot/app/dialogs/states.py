from aiogram.fsm.state import StatesGroup, State


class MenuSG(StatesGroup):
    main = State()


class InfoSG(StatesGroup):
    main = State()


class CampSG(StatesGroup):
    choice = State()
    main = State()
