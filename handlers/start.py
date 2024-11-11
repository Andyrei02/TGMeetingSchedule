# Copyright (c) 2023 Andrei Cenușă
# All rights reserved.
#
# This code is licensed under the MIT License.
# See LICENSE for details.


from aiogram import types, html
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F

from utils.loader import dp, db
from utils.logger import setup_logger


logger = setup_logger(__name__)

@dp.message(Command("start"))
async def start(message):
	# Send a welcome message to the user
	logger.info(f"Add user: {message.from_user.id}")
 
	kb = [
		[
		types.KeyboardButton(text="other project"),
		types.KeyboardButton(text="contact links")
		],
	]
	keyboard = types.ReplyKeyboardMarkup(
		keyboard=kb,
		resize_keyboard=True,
		input_field_placeholder="Select option"
    )

	start_message = f"Hello {html.bold(html.quote(message.from_user.full_name))}"
	await message.answer(start_message, reply_markup=keyboard)

	try:
		await add_user(message)
	except Exception as e:
		logger.error("Error processing 'ADD USER': %s", e)


@dp.message(F.text.lower() == "contact links")
async def with_puree(message: types.Message):
	builder = InlineKeyboardBuilder()
	builder.row(types.InlineKeyboardButton(
		text="GitHub", url="https://github.com/Andyrei02/")
	)
	builder.row(types.InlineKeyboardButton(
		text="Instagram", url="https://www.instagram.com/andr.ei57/")
	)
	builder.row(types.InlineKeyboardButton(
		text="Telegram", url="tg://user?id=749333822")
	)
	await message.answer(
		"My links:",
		reply_markup=builder.as_markup(),
	)

async def add_user(message):
	await db.connect()

	# Add a user
	user = (message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username, '', '', '')
	await db.add_user(user)

	# Close the database connection
	await db.close()
