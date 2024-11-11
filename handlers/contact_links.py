from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.loader import dp


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
