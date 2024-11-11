from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.loader import dp


@dp.message(F.text.lower() == "other project")
async def with_puree(message: types.Message):
	builder = InlineKeyboardBuilder()
	builder.row(types.InlineKeyboardButton(
		text="GeoApp", url="https://geoapp.up.railway.app/")
	)
	await message.answer(
		"My projects:",
		reply_markup=builder.as_markup(),
	)
