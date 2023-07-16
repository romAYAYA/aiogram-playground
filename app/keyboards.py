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
    InlineKeyboardButton(text="Astana-Almaty", callback_data='Astana-Almaty'),
    InlineKeyboardButton(text="Toronto-Tokyo", callback_data='Toronto-Tokyo'),
    InlineKeyboardButton(text="Kiev-Berlin", callback_data="Kiev-Berlin"),
)
