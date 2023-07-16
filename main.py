import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from app import keyboards as kb
from app import database as db

load_dotenv()
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher(bot=bot)


async def on_startup(_):
    await db.db_start()
    print('Bot activated')


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    """Starts the bot"""
    await db.cmd_start_db(message.from_user.id)
    await message.answer_sticker(
        "CAACAgIAAxkBAAMVZKVO9Twjk_6m39R8Nm50KHkWJhsAAoUAA8GcYAyLjB0fSFNdIi8E"
    )
    await message.answer(
        f"Welcome to the club, {message.from_user.first_name}!", reply_markup=kb.main
    )

    if message.from_user.id == int(os.getenv("ADMIN_ID")):
        await message.answer("You entered admin mode", reply_markup=kb.main_admin)


@dp.message_handler(text="Tickets")
async def get_tickets(message: types.Message):
    """Shows menu"""
    await message.answer("Sorry, anything left", reply_markup=kb.tickets_list)


@dp.message_handler(text="Cart")
async def get_cart(message: types.Message):
    """Shows the cart"""
    await message.answer("Your cart is empty")


@dp.message_handler(text="Admin")
async def get_admin_panel(message: types.Message):
    """Shows admin panel"""
    if message.from_user.id == int(os.getenv("ADMIN_ID")):
        await message.answer("You entered admin mode", reply_markup=kb.admin_panel)
    else:
        await message.answer_sticker(
            "CAACAgIAAxkBAAMiZKVStZZorGto_KnKzvCGd0-nerQAAhYAAzed7hJaF5ONGLk2Qi8E"
        )
        await message.answer("Can't get you, brother")


@dp.message_handler()
async def unknown_answer(message: types.Message):
    """Answers unknown message"""
    await message.answer_sticker(
        "CAACAgIAAxkBAAMiZKVStZZorGto_KnKzvCGd0-nerQAAhYAAzed7hJaF5ONGLk2Qi8E"
    )
    await message.answer("Can't get you, brother")


@dp.callback_query_handler()
async def callback_query_keyboard(callback_query: types.CallbackQuery):
    if callback_query.data == 'Astana-Almaty':
        await bot.send_message(chat_id=callback_query.from_user.id, text='You bocked ticket from Astana to Almaty')
    elif callback_query.data == 'Toronto-Tokyo':
        await bot.send_message(chat_id=callback_query.from_user.id, text='You bocked ticket from Toronto to Tokyo')
    elif callback_query.data == 'Kiev-Berlin':
        await bot.send_message(chat_id=callback_query.from_user.id, text='You bocked ticket from Kiev to Berlin')


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
