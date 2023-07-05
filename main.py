import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from aiogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

load_dotenv()
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher(bot=bot)

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add("Menu").add("Cart").add("Donate")

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add("Menu").add("Cart").add("Donate").add("Admin")

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add("Add item").add("Delete item").add("Mail")


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    """Starts the bot"""
    await message.answer_sticker(
        "CAACAgIAAxkBAAMVZKVO9Twjk_6m39R8Nm50KHkWJhsAAoUAA8GcYAyLjB0fSFNdIi8E"
    )
    await message.answer(
        f"Welcome to the club, {message.from_user.first_name}!", reply_markup=main
    )

    if message.from_user.id == int(os.getenv("ADMIN_ID")):
        await message.answer("You entered admin mode", reply_markup=main_admin)


@dp.message_handler(text="Donate")
async def get_donation_info(message: types.Message):
    """Sends info for donation"""
    await message.answer("Kaspi: +7055166184")


@dp.message_handler(text="Menu")
async def get_menu(message: types.Message):
    """Shows menu"""
    await message.answer("Sorry, anything left")


@dp.message_handler(text="Cart")
async def get_cart(message: types.Message):
    """Shows the cart"""
    await message.answer("Your cart is empty")


@dp.message_handler(text="Admin")
async def get_admin_panel(message: types.Message):
    """Shows admin panel"""
    if message.from_user.id == int(os.getenv("ADMIN_ID")):
        await message.answer("You entered admin mode", reply_markup=admin_panel)
    else:
        await message.answer_sticker(
            "CAACAgIAAxkBAAMiZKVStZZorGto_KnKzvCGd0-nerQAAhYAAzed7hJaF5ONGLk2Qi8E"
        )
        await message.answer("Can't get you, brother")


@dp.message_handler(content_types=["document", "photo"])
async def forward_message(message: types.Message):
    """Forwards photos and documents"""
    await bot.forward_message(
        os.getenv("GROUP_ID"), message.from_user.id, message.message_id
    )


@dp.message_handler()
async def unknown_answer(message: types.Message):
    """Answers unknown message"""
    await message.answer_sticker(
        "CAACAgIAAxkBAAMiZKVStZZorGto_KnKzvCGd0-nerQAAhYAAzed7hJaF5ONGLk2Qi8E"
    )
    await message.answer("Can't get you, brother")


if __name__ == "__main__":
    executor.start_polling(dp)
