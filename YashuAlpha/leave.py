from config import DEV
from .data import KeshavX
from .verify import verify
from pyrogram import Client, filters
from . import hl

LEGENDS = DEV.SUDO_USERS + [DEV.OWNER_ID] + KeshavX

@Client.on_message(filters.command("leave", hl))
async def leave(_, m):
    if not await verify(m.from_user.id):
        return
    try:
        id = int(m.text.split()[1])
    except:
        id = m.chat.id
    await m.reply("LEFT CHAT ✅ ")
    await _.leave_chat(id)
    
