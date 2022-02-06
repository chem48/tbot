from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


#клава для записи и удаления в базу
button_load = KeyboardButton('/load')
button_delete = KeyboardButton('/cancel')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete)