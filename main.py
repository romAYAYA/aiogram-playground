import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from app import keyboards as kb
from app import database as db

storage = MemoryStorage()
load_dotenv()
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher(bot=bot, storage=storage)


async def on_startup(_):
    await db.db_start()
    print('Bot activated')


async def get_tickets_list_keyboard():
    db.cur.execute("SELECT direction, fly_date, price FROM tickets")
    tickets = db.cur.fetchall()

    tickets_list = types.InlineKeyboardMarkup(row_width=1)

    for ticket in tickets:
        direction = ticket[0]
        fly_date = ticket[1]
        price = ticket[2]
        button_text = f"{direction} - {fly_date} - {price}$"
        button = types.InlineKeyboardButton(text=button_text, callback_data=direction)
        tickets_list.add(button)

    return tickets_list



@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    """Starts the bot"""
    await message.answer(
        f"Welcome to the club, {message.from_user.first_name}!", reply_markup=kb.main
    )


@dp.message_handler(text="Tickets")
async def get_tickets(message: types.Message):
    """Shows menu"""
    tickets_list = await get_tickets_list_keyboard()
    if tickets_list:
        await message.answer('Available tickets:', reply_markup=tickets_list)
    else:
        await message.answer("No tickets available at the moment.")


@dp.callback_query_handler()
async def handle_ticket_selection(callback_query: types.CallbackQuery):
    ticket_direction = callback_query.data
    await bot.send_message(callback_query.from_user.id, f"The ticket for {ticket_direction} is booked!")
    await callback_query.answer()

@dp.message_handler()
async def unknown_answer(message: types.Message):
    """Answers unknown message"""
    await message.answer_sticker(
        "CAACAgIAAxkBAAMiZKVStZZorGto_KnKzvCGd0-nerQAAhYAAzed7hJaF5ONGLk2Qi8E"
    )
    await message.answer("Can't get you, brother")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
