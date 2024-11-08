# Copyright (c) 2023 Andrei Cenușă
# All rights reserved.
#
# This code is licensed under the MIT License.
# See LICENSE for details.

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from utils import config
from utils.users_database import UserDatabase

bot = Bot(
    token=config.TELEGRAM_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

db = UserDatabase(config.db_config)
