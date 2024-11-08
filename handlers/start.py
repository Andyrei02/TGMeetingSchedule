# Copyright (c) 2023 Andrei Cenușă
# All rights reserved.
#
# This code is licensed under the MIT License.
# See LICENSE for details.

from utils.loader import dp, db
from aiogram.filters.command import Command


@dp.message(Command("start"))
async def start(message):
	# Send a welcome message to the user
	await message.answer("<b>Hello!</b>")

	# await add_user(message)


async def add_user(message):
	await db.connect()

	# Add a user
	user = (message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username, '', '', '')
	await db.add_user(user)

	# Close the database connection
	await db.close()
