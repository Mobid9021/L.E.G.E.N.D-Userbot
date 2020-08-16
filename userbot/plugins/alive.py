import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/e5c4be66f4c034560b736.jpg"
pm_caption = "**L.E.G.E.N.D is online**\n"

pm_caption += "\n**My Legendary Boss**            : @The_Anonymous_Legend\n"

pm_caption += "\n**Telethon Version**            : 4.8\n"

pm_caption += "\n**Python Version**            : 3.8.5\n"

pm_caption += "\nI am a cool userbot with many functions managed by [this legendary person.](https://t.me/The_Anonymous_Legend) Contact him for any help or support\n"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
