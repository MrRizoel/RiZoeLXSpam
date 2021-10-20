from .. import Riz, SUDO_USERS
from telethon import events
from time import time
from datetime import datetime

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)
    
HELP_PIC = "https://telegra.ph/file/9acc785291052c8f8998d.jpg"
@Riz.on(events.NewMessage(pattern=".help"))
async def help(event):
    if event.sender_id in SMEX_USERS:
     await e.reply(text, parse_mode=None, link_preview=None )
     await Riz.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=" 🔥 𝗥𝗜𝗭𝗢𝗘𝗟 𝗫 𝗦𝗣𝗔𝗠 🔥\n\nᴄᴍᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ʀɪᴢᴏᴇʟ x sᴘᴀᴍ\n\n ↧ 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙲𝙼𝙳𝚂 ↧\n\n .ping - to check ping\n .alive - to check bot alive/version (only main userbot will reply)\n .setname - to change Name\n .inviteall - to add members using spam bots\n .restart - to restart all spam bots\n\n ↧ 𝙹𝙾𝙸𝙽/𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳𝚂 ↧\n\n .join - to join public channel/groups\n .pjoin - to join public channel/groups\n .leave - to leave public/private channel/groups\n\n ↧ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧\n\n.raid - to raid\n .replyraid - to active reply raid\n .dreplyraid - to de-active reply raid\n .spam - this cmd use for Normal spam\n .bigspam - this cmd use for big spam\n .delayspam - this cmd use for delay spam\n\n ALL CMDS WITH DETAILS [HERE.]()\n\n© @RiZoeLX | @DNHxHELL"                                     )                                                         