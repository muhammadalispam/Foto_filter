from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def start_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.add(
        KeyboardButton(text="💫Rasmga Effect berish"),
        KeyboardButton(text="👤Adminstratorga muloqot"),
    )
    return btn


async def filters_btn(filters: list):
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.add(
        KeyboardButton(text="⬅️Ortga"),
    )
    btn.add(
        *[KeyboardButton(text=item) for item in filters]
    )

    return btn


async def cansle_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)

    btn.add(
        KeyboardButton(text="❌Bekor qilish"),
        KeyboardButton(text="⬅️Ortga"),
    )
    return btn

