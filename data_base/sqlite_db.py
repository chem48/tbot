import sqlite3 as sq
from create_bot import dp, bot

def sql_start():
	global base, cur
	base = sq.connect('answ.db')
	cur = base.cursor()
	if base:
		print ('Соединение с базой answ.db установлено!')
	base.execute('CREATE TABLE IF NOT EXISTS spisok(img TEXT, quest TEXT PRIMARY KEY, answer TEXT, ilink TEXT)')
	base.commit()


async def sql_add_command(state):
	async with state.proxy() as data:
		cur.execute('INSERT INTO spisok VALUES (?,?,?,?)', tuple(data.values()))
		base.commit()

async def sql_read(message):
	for record_db in cur.execute('SELECT * FROM spisok').fetchall():
		await bot.send_photo(message.from_user.id, record_db[0], f'{record_db[1]}, {record_db[2]}, {record_db[3]}')
