# Copyright (c) 2023 Andrei Cenușă
# All rights reserved.
#
# This code is licensed under the MIT License.
# See LICENSE for details.

import logging
import os
import asyncio
import aiogram

from utils.loader import dp, bot
import handlers


logging.basicConfig(level=logging.INFO)

async def main():
	await dp.start_polling(bot)


if __name__ == '__main__':
	asyncio.run(main())