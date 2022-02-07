from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb
from data_base import read_db


ID = None

class FSMAdmin(StatesGroup):
	photo = State()
	quest_admin = State()	
	answer_admin = State()
	ilink = State()

#ID админа
async def make_changes_command(message:types.Message):
	global ID
	ID=message.from_user.id
	await bot.send_message(message.from_user.id, 'Бот готово к управлению!', reply_markup = admin_kb.button_case_admin)
	await message.delete()


#чтение информации из базы данных
async def admin_read_db(message : types.Message): 
	print('Чтение')
	await bot.send_message(message.from_user.id, 'Запущена процедура чтения записей из базы')
	print('Отправлена команда Чтение от пользователя', message.from_user.username)
	read_sqlite_table()


#Начало записи сообщений

#@dp.message_handler (command ='Загрузить', state=None)
async def admin_start(message : types.Message):
	#if message.from_user.id==ID: 
	await bot.send_message(message.from_user.id, 'Запущена процедура записи Вопроса.')
	print('Отправлена команда Загрузить от пользователя', message.from_user.username)
	await FSMAdmin.photo.set()
	await message.reply('Загрузи фото')

	#Ответ от админа
#@dp.message_handler(content_types=['photo'], state=FSAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
	if message.from_user.id==ID: 
		async with state.proxy() as data:
			data['photo'] = message.photo[0].file_id
		await FSMAdmin.next()
		await message.reply ('Введи вопрос')

#@dp.message_handler(state=FSAdmin.quest_admin)
async def load_quest(message: types.Message, state: FSMContext):
	if message.from_user.id==ID: 
		async with state.proxy() as data:
			data['quest_admin'] = message.text
		await FSMAdmin.next()
		await message.reply ('Введи ответ')

async def load_answer(message: types.Message, state: FSMContext):
	if message.from_user.id==ID: 
		async with state.proxy() as data:
			data['answer_admin'] = message.text
		await FSMAdmin.next()
		await message.reply ('Введи ссылку')



#@dp.message_handler(state=FSAdmin.ilink)
async def load_ilink(message: types.Message, state: FSMContext):
	if message.from_user.id==ID: 
		async with state.proxy() as data:
			data['ilink'] = message.text
		#async with state.proxy() as data:
		#	await message.reply(str(data))
		await sqlite_db.sql_add_command(state) #запись в базу данных
		await state.finish()

#Выход из состояния
async def cancel_handler(message:types.Message,state:FSMContext):
	#if message.from_user.id==ID: 
	current_state =await state.get_state()
	if current_state is None:
		return
	await state.finish()
	await message.reply('ОК')
	print('Загрузка отменена пользователем ', message.from_user.username)



def register_handlers_admin(dp : Dispatcher):
	#dp.register_message_handler(command_start, commands=['start','help'])
	dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
	dp.register_message_handler(cancel_handler, state="*", commands=['отмена'])
	dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")

	dp.register_message_handler(admin_start, commands=['load','adm'])
	dp.register_message_handler(admin_read_db, commands=['read'])
	dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
	dp.register_message_handler(load_quest, state=FSMAdmin.quest_admin)	
	dp.register_message_handler(load_answer, state=FSMAdmin.answer_admin)
	dp.register_message_handler(load_ilink, state=FSMAdmin.ilink)