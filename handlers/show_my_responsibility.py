from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.loader import dp


@dp.message(F.text.lower() == "show my responsibility")
async def with_puree(message: types.Message):
	await message.answer(
		"My responibility:",
	)
