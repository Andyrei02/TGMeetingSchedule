# Copyright (c) 2023 Andrei Cenușă
# All rights reserved.
#
# This code is licensed under the MIT License.
# See LICENSE for details.

import logging
import os
import asyncio
import aiogram

from utils.logger import setup_logger
from utils.loader import dp, bot
import handlers


logger = setup_logger(__name__, level=logging.INFO)

async def main():
	logger.info("Bot is starting...")

	await dp.start_polling(bot)
	logger.info("Bot setup completed.")


if __name__ == '__main__':
	asyncio.run(main())