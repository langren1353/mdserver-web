import sys
import io
import os
import time
import re
import json
import base64
import threading
import asyncio

sys.path.append(os.getcwd() + "/class/core")
import mw

import telebot
from telebot import types
from telebot.util import quick_markup


chat_id = -1001578009023


async def run(client):
    while True:

        await client.send_message(chat_id, 'Hello, group!')
        print("123123" + str(time.time()))
        await asyncio.sleep(1)


if __name__ == "__main__":
    pass
