from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db


async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Социальный контракт.', reply_markup=kb_client)
		await message.delete()
		print('Сообщение start удалено')
	except:
		await message.reply('Напишите в личку боту')	


async def send(message : types.Message):
	if message.text == 'Привет':
		await message.reply('И тебе привет')


	if message.text == 'Что такое социальный контракт? 👋':
		await sqlite_db.sql_read(message)
		#await bot.send_photo(p.from_user.id, open('d:/Github/Python/tbot/img/img1.jpg', 'rb'))
		await bot.send_message(message.from_user.id, 'Социальный контракт – это договор,'
													 'по которому орган социальной защиты предоставляет '
													 'денежную помощь, а граждане обязуются улучшить своё '
													 'материальное положение в рамках реализации мероприятий'
													 'по заключенному договору.')
	
		bot.send_message(message.from_user.username, 'Тестовое сообещение по первому вопросу')
		print ('задан вопрос 1 пользователем ', message.from_user.username)

	if message.text == 'Кто может обратиться?':
		await bot.send_message(message.from_user.id, 'Граждане РФ, проживающие в Белгородской области,'
			'которые имеют среднедушевой доход семьи'
			'(одиноко проживающего гражданина) ниже величины прожиточного'
			'минимума (ВПМ), установленного в Ленинградской области.'
			'ВПМ для трудоспособного населения - 11 586,00 руб.'
			'ВПМ для пенсионеров - 9141,00 руб.'
			'ВПМ для детей - 10 310,00 руб.')

	if message.text == 'Направления оказания помощи.':
		await bot.send_message(message.from_user.id, 'Развитие ИП, ЛПХ, Трудоустройство, Трудная жизненная ситуация')



#	
def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands=['start','help'])	
	dp.register_message_handler(send)