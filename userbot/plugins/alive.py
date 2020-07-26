"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://github.com/jarvis210904/J.A.R.V.I.S-Userbot/blob/master/jarvis.jpg?raw=true"
pm_caption = "`JARVIS STATUS:` **ONLINE**\n\n"
pm_caption += "**Support Channel** : [🔰Join Support Channel🔰](https://t.me/jarvissupportofficial)\n\n"
pm_caption += "**Support Group** : [🔰Join Support Group🔰](https://t.me/joinchat/R5-ZBEdh9Uzix53RWtmHiA)\n\n"

pm_caption += "**SYSTEM STATUS**\n\n"
pm_caption += "`TELETHON VERSION:` **6.0.9**\n`Python:` **3.7.4**\n\n"
pm_caption += "`DATABASE STATUS:` **Functional**\n\n"
pm_caption += "**Current Branch** : `master`\n\n"
pm_caption += "**JARVIS OS** : `3.25`\n\n"
pm_caption += "**Current Sat** : `JARVISSat-2.25`\n\n"
pm_caption += f"**My Boss** : {DEFAULTUSER} \n\n"
pm_caption += "**Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "**License** : [MIT Licence](https://github.com/jarvis210904/J.A.R.V.I.S-Userbot/blob/master/LICENSE)\n\n"
pm_caption += "Copyright : By [JARVIS@Github](GitHub.com/jarvis210409)\n\n\n\n"
pm_caption += " [Deploy JARVIS](https://telegra.ph/JARVIS-UserBot-07-26)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
    
