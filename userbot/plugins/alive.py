"""Check if userbot alive."""
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/Anonymous-07-25"
pm_caption = "`💠JARVIS IS💠:` **ONLINE**\n\n"
pm_caption += "**🔖SYSTEM STATUS🔖**\n\n"
pm_caption += "`⚖️TELETHON VERSION⚖️:` **6.0.9**\n`Python:` **3.7.4**\n\n"
pm_caption += "`🎢DATABASE STATUS🎢:` **Functional**\n\n"
pm_caption += "**🧮Current Branch🧮** : `master`\n\n"
pm_caption += "**📬JARVIS OS📬** : `3.14`\n\n"
pm_caption += "**💡Current Sat💡** : `StarkGangSat-2.25`\n\n"
pm_caption += f"*💜*My Boss💜** : {DEFAULTUSER} \n\n"
pm_caption += "**💥Heroku Database💥** : `AWS - Working Properly`\n\n"
pm_caption += "**🚫License🚫** : [MIT Licence](github.com/StarkGang/FridayUserbot/blob/master/LICENSE)\n\n"
pm_caption += "⛔️Copyright : By⛔️ [StarkGang@Github](GitHub.com/StarkGang)\n\n\n\n"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption
    
