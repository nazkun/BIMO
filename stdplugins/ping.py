import asyncio
import json
import math
import os
import time
from datetime import datetime
from telethon import events
from uniborg.util import admin_cmd, progress, humanbytes


@borg.on(admin_cmd(pattern="ping ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.reply("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000000
    await event.edit("`Pong speed⚡️` !\n{}".format(ms))
