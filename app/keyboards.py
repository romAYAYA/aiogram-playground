from aiogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add("Tickets").add("Cart")

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add("Tickets").add("Cart").add("Admin")

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add("Add item").add("Delete item").add("Mail")

tickets_list = InlineKeyboardMarkup(row_width=2)
tickets_list.add(
    InlineKeyboardButton(text="Astana-Almaty", url="https://chat.openai.com/"),
    InlineKeyboardButton(text="Toronto-Tokyo", url="https://chat.openai.com/"),
    InlineKeyboardButton(text="Kiev-Berlin", url="https://chat.openai.com/"),
)
