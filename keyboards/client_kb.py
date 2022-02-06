from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


#b0 = KeyboardButton('/start')
b1 = KeyboardButton("Что такое социальный контракт? 👋")
b2= KeyboardButton("Кто может обратиться?")
b3 = KeyboardButton('Направления оказания помощи.')

b10 = KeyboardButton("Отправить номер для обратной связи.", request_contact=True)
b11 = KeyboardButton('Отправить информацию о своем районе.', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).add(b3).row(b10,b11)