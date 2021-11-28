from .. import Riz, SUDO_USERS
from telethon import events
from time import time
from datetime import datetime

    
HELP_PIC = "https://telegra.ph/file/9acc785291052c8f8998d.jpg"

RiZoeLX = "🔥 𝗥𝗜𝗭𝗢𝗘𝗟 𝗫 𝗦𝗣𝗔𝗠 🔥\n\n"
 
RiZoeLX += f"__ᴄᴍᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ʀɪᴢᴏᴇʟ x sᴘᴀᴍ__\n\n"

RiZoeLX += f" ↧ 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙲𝙼𝙳𝚂 ↧\n\n"

RiZoeLX += f" `.ping` - to check ping\n `.alive` - to check bot alive/version (only main userbot will reply)\n `.setname` - to change Name\n .`inviteall` - to add members using spam bots\n .`restart` - to restart all spam bots\n\n"
 
RiZoeLX += f" ↧ 𝙹𝙾𝙸𝙽/𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳𝚂 ↧\n\n"

RiZoeLX += f" `.join` - to join public channel/groups\n `.pjoin` - to join public channel/groups\n `.leave` - to leave public/private channel/groups\n\n"
 
RiZoeLX += f" ↧ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧\n\n"

RiZoeLX += f" `.raid` - to raid\n `.replyraid` - to active reply raid\n `.dreplyraid` - to de-active reply raid\n `.spam` - this cmd use for Normal spam\n `.bigspam` - this cmd use for big spam\n `.delayspam` - this cmd use for delay spam\n\n"
 
RiZoeLX += f"ALL CMDS WITH DETAILS [HERE.](https://telegra.ph/%F0%9D%97%A5%F0%9D%97%9C%F0%9D%97%AD%F0%9D%97%A2%F0%9D%97%98%F0%9D%97%9F-%F0%9D%97%AB-%F0%9D%97%A6%F0%9D%97%A3%F0%9D%97%94%F0%9D%97%A0-10-15)\n\n"
 
RiZoeLX += f"© @RiZoeLX | @DNHxHELL\n"


@Riz.on(events.NewMessage(pattern=r"\.help"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=RiZoeLX)                                                         
