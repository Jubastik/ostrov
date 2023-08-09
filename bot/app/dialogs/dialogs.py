import asyncio
import logging

from aiogram import Router
from aiogram.dispatcher.event.bases import UNHANDLED
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram_dialog import Dialog, DialogManager, StartMode
from aiogram_dialog.api.exceptions import UnknownIntent
from aiohttp import ClientConnectorError

from app.dialogs.states import MenuSG
from app.dialogs.windows.camp.camp import CampChoiceWin, CampDerailedWin
from app.dialogs.windows.info.info import InfoMainWin
from app.dialogs.windows.menu.menu import MenuMainWin

dlg_router = Router()


@dlg_router.message(CommandStart())
async def handle_start_query(message: Message, dialog_manager: DialogManager):
    await message.answer('''Добро пожаловать на остров Кильпола! Расположенный в сердце национального парка "Ладожские шхеры" на озере Ладога, этот остров предлагает уникальное сочетание природного величия и культурного наследия. 
	Остров Кильпола славится своей захватывающей красотой природы. Здесь вы будете поражены мощью и величием ладожских скал, которые украшают пейзаж острова. Густые леса, залитые солнечным светом, создают уютное атмосферное окружение, приглашая вас на прогулки и пешие экскурсии.
	''')
    await message.answer('''Остров Кильпола предлагает богатый выбор активностей для всех любителей приключений. Вы можете исследовать пешие маршруты, наслаждаться кемпингами или покататься на каяках по окружающим острову водам. Для тех, кто ищет расслабление и умиротворение, здесь можно провести время, наслаждаясь пляжами, устраивая пикники или просто наблюдая за захватывающими закатами.
	Культурное наследие острова Кильпола привлекает не только своими уникальными природными памятниками. Вы можете посетить музей Кильполы, где вы сможете узнать больше о культуре и традициях этого места.
	Ситус.центр острова Кильпола предлагает всю необходимую информацию для планирования вашей поездки. Здесь вы найдете карты маршрутов, информацию о достопримечательностях, размещении и рекомендациях о питании. Мы поможем вам воплотить ваше приключение на острове Кильпола в незабываемый опыт, который оставит глубокое впечатление.
''')
    await starting_dispatcher(message, dialog_manager)


@dlg_router.message(Command("update"))
async def handle_update_query(message: Message, dialog_manager: DialogManager):
    await starting_dispatcher(message, dialog_manager)


async def starting_dispatcher(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MenuSG.main, mode=StartMode.RESET_STACK)


@dlg_router.message(Command("start"))
async def handle_ping(message: Message):
    await message.reply("pong🟢")


async def error_handler(event, dialog_manager: DialogManager):
    logging.error(event.exception)
    if isinstance(event.exception, UnknownIntent):
        # Handling an error related to an outdated callback
        await handle_update_query(event.update.callback_query, dialog_manager)
    elif isinstance(event.exception, ClientConnectorError):
        await event.update.callback_query.answer("Сервер недоступен", show_alert=True)
    else:
        return UNHANDLED


MenuDLG = Dialog(MenuMainWin)
InfoDLG = Dialog(InfoMainWin)
CampDLG = Dialog(CampChoiceWin, CampDerailedWin)
