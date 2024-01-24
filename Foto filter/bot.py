import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib. fsm_storage.memory import MemoryStorage
from state import *
from database import *
from utills import *
from btn import *


BOT_TOKEN = "6881487545:AAEL7lbncdLWvB8Y_bVd74WUZG1RK7cqD7o"
ADMINS = [127158713]

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)


async def command_menu(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Ishga tushirish'),
            types.BotCommand('help', 'Yordam'),
            types.BotCommand('statisticks', 'Yordam'),
        ]
    )


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await add_user(
        user_id=message.from_user.id,
        username=message.from_user.username
    )
    btn = await start_btn()
    await message.answer(f"Assalomu aleykum ❗️{message.from_user.first_name}❗️ \n"
                         f"Men ❗️Filtering_bot❗️ man Siz menga biron bir rasm tashlasangiz\n"
                         f"Siz xoxlagandek qilib beraman \n"
                         f"Uning uchun menulardan birini tanlang ❗️❗️", reply_markup=btn)


@dp.message_handler(commands=["statisticks"])
async def get_user_stat_hendler(message: types.Message):
    if message.from_user.id in ADMINS:
        count = await get_all_user()
        await message.answer(f"❗️Filtering_bot❗️ botining a'zolari soni: 👉{count}👈 ni tashkil etadi")
    else:
        await message.answer(f"❗️Filtering_bot❗️ botining a'zolari soni faqat bot adminiga korinadi‼️‼️")


@dp.message_handler(text="💫Rasmga Effect berish")
async def effect_to_emage_handler(message: types.Message):
    btn = await filters_btn(filters)
    await message.answer(f"Filterlardan birini tanlang:👇👇", reply_markup=btn)


@dp.message_handler(text="⬅️Ortga")
async def back_handler(message: types.Message):
    await start_command(message)


@dp.message_handler(content_types="text")
async def selected_filter_handler(message: types.Message, state: FSMContext):
    text = message.text

    if text in filters:
        await state.update_data(filter=text)
        btn = await cansle_btn()
        await message.answer("Iltimos menga rasm yuboring 😊", reply_markup=btn)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=command_menu)
