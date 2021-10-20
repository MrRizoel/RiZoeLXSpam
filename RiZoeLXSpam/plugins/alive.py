from .. import Riz, SUDO_USERS
from telethon import events
from time import time
from datetime import datetime

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)
    
RIZ_PIC = "https://telegra.ph/file/db194f99e15db50f43c72.jpg"
@Riz.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SMEX_USERS:
     await e.reply(text, parse_mode=None, link_preview=None )
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption="✧ 𝑅𝐼𝑍𝑂𝐸𝐿 𝑋 𝑆𝑃𝐴𝑀 𝐼𝑍𝑍 𝐴𝐿𝐼𝑉𝐸𝐸 ✧\n\n ┏━━━━━━━━━━━━━━━━━━━\n ┣➣ ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : 3.9.6\n ┣➣ ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : 1.17\n ┣➣ sᴜᴘᴘᴏʀᴛ : [JOIN](https://t.me/DNHxHELL)\n ┣➣ ᴄʜᴀɴɴᴇʟ : [JOIN](https://t.me/RiZoeLX)\n ┗━━━━━━━━━━━━━━━━━━━\n\n 🖤 [𝐑𝐄𝐏𝐎](https://github.com/MrRizoel/RiZoeLXSpam) 🖤"                                
                              )