# Copyright (c) 2023 Andrei Cenușă
# All rights reserved.
#
# This code is licensed under the MIT License.
# See LICENSE for details.

import os
from dotenv import load_dotenv


load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')

if TELEGRAM_TOKEN is None:
	raise ValueError("Telegram API token not found in environment variables")

if not os.path.exists('data'): os.mkdir('data')

db_host = os.getenv('PGHOST')
db_port = os.getenv('PGPORT')
db_database = os.getenv('PGDATABASE')
db_username = os.getenv('PGUSER')
db_password = os.getenv('PGPASSWORD')

db_config = {
	'user': db_username,
	'password': db_password,
	'host': db_host,
	'port': db_port,
	'database': db_database
}

DEBUG = True