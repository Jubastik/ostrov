from random import choice

from aiogram.types import Message
from aiogram_dialog import DialogManager, DialogProtocol

# from app.dialogs.universal_methods import get_tg_id_from_manager

stickers = ['👍', '👻', '😄', '🧐', '👀', '🌝', '🎫', '🔫', '📌', '📚']


async def getter_menu(dialog_manager: DialogManager, **kwargs):
    tg_id = "1234567890"
    return {"name": "Олег",
            "sticker": choice(stickers),
            }
