#стартовый файл
from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db
from data_base import read_db


async def on_startup(_):
	print ('Нафаня в сети')
	sqlite_db.sql_start()
	#read_db.read_sqlite_table()

from handlers import client, admin, other


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
#other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)