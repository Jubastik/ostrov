from random import choice

from aiogram.types import Message
from aiogram_dialog import DialogManager, DialogProtocol

# from app.dialogs.universal_methods import get_tg_id_from_manager

stickers = ['👍', '👻', '😄', '🧐', '👀', '🌝', '🎫', '🔫', '📌', '📚']


async def getter_menu(dialog_manager: DialogManager, **kwargs):
    name = kwargs["event_from_user"].first_name
    return {"name": name,
            "sticker": choice(stickers),
            }
