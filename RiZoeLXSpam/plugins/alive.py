from .. import Riz, SUDO_USERS
from .. import ALIVE_PIC
from telethon import events
from time import time
from datetime import datetime

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/ba87c58f01a6fcb5ef512.jpg"
  

          
rizoel = "✧ 𝑅𝐼𝑍𝑂𝐸𝐿 𝑋 𝑆𝑃𝐴𝑀 𝐼𝑍𝑍 𝐴𝐿𝐼𝑉𝐸𝐸 ✧\n\n"

rizoel += f"┏━━━━━━━━━━━━━━━━━━━\n"

rizoel += f"┣➣ ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : `3.9.6`\n"

rizoel += f"┣➣ ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : `1.17`\n"
    
rizoel += f"┣➣ sᴜᴘᴘᴏʀᴛ : [JOIN](https://t.me/DNHxHELL)\n"

rizoel += f"┣➣ ᴄʜᴀɴɴᴇʟ : [JOIN](https://t.me/RiZoeLX)\n"

rizoel += f"┗━━━━━━━━━━━━━━━━━━━\n\n"

rizoel += f"🖤 [𝐑𝐄𝐏𝐎](https://github.com/MrRizoel/RiZoeLXSpam) 🖤"            
                                    
@Riz.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SMEX_USERS:
     await event.reply(text, parse_mode=None, link_preview=None )
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel)
    
