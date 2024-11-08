# Copyright (c) 2023 Andrei Cenușă
# All rights reserved.
#
# This code is licensed under the MIT License.
# See LICENSE for details.


from aiogram import html
from aiogram.filters.command import Command

from utils.loader import dp, db
from utils.logger import setup_logger


logger = setup_logger(__name__)

@dp.message(Command("start"))
async def start(message):
	# Send a welcome message to the user
	logger.info(f"Add user: {message.from_user.id}")

	start_message = f"Hello {html.bold(html.quote(message.from_user.full_name))}"
	await message.answer(start_message)

	try:
		await add_user(message)
	except Exception as e:
		logger.error("Error processing 'ADD USER': %s", e)


async def add_user(message):
	await db.connect()

	# Add a user
	user = (message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username, '', '', '')
	await db.add_user(user)

	# Close the database connection
	await db.close()
