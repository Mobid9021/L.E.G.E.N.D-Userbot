import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/e5c4be66f4c034560b736.jpg"
pm_caption = "**L.E.G.E.N.D is ONLINE**\n"

pm_caption += f"\n**My Legendary Boss**: {DEFAULTUSER}\n"

pm_caption += "\nTelethon Version: 4.8\n"

pm_caption += "\nPython Version: 3.8.5\n"

pm_caption += "\nLicense: [AGPL-3.0 Licence](https://github.com/KeshavTech246/L.E.G.E.N.D-userbot/blob/master/LICENSE/)\n"

pm_caption += "\nCopyright by: [L.E.G.E.N.D](https://github.com/KeshavTech246)\n"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
