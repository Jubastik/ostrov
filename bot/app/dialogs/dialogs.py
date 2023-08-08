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
    await starting_dispatcher(message, dialog_manager)


async def starting_dispatcher(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MenuSG.main, mode=StartMode.RESET_STACK)


@dlg_router.message(Command("ping"))
async def handle_ping(message: Message):
    await message.reply("pong🟢")


async def error_handler(event, dialog_manager: DialogManager):
    logging.error(event.exception)
    if isinstance(event.exception, UnknownIntent):
        # Handling an error related to an outdated callback
        await handle_start_query(event.update.callback_query, dialog_manager)
    elif isinstance(event.exception, ClientConnectorError):
        await event.update.callback_query.answer("Сервер недоступен", show_alert=True)
    else:
        return UNHANDLED


MenuDLG = Dialog(MenuMainWin)
InfoDLG = Dialog(InfoMainWin)
CampDLG = Dialog(CampChoiceWin, CampDerailedWin)