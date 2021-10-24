import asyncio
from .. import Riz, Riz2, Riz3, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20
from RiZoeLXSpam.config import SUDO_USERS
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon import events
import os
import random
import sys

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)


@Riz.on(events.NewMessage(pattern=".join"))
@Riz2.on(events.NewMessage(pattern=".join"))
@Riz3.on(events.NewMessage(pattern=".join"))
@Riz4.on(events.NewMessage(pattern=".join"))
@Riz5.on(events.NewMessage(pattern=".join"))
@Riz6.on(events.NewMessage(pattern=".join"))
@Riz7.on(events.NewMessage(pattern=".join"))
@Riz8.on(events.NewMessage(pattern=".join"))
@Riz9.on(events.NewMessage(pattern=".join"))
@Riz10.on(events.NewMessage(pattern=".join"))
@Riz11.on(events.NewMessage(pattern=".join"))
@Riz12.on(events.NewMessage(pattern=".join"))
@Riz13.on(events.NewMessage(pattern=".join"))
@Riz14.on(events.NewMessage(pattern=".join"))
@Riz15.on(events.NewMessage(pattern=".join"))
@Riz16.on(events.NewMessage(pattern=".join"))
@Riz17.on(events.NewMessage(pattern=".join"))
@Riz18.on(events.NewMessage(pattern=".join"))
@Riz19.on(events.NewMessage(pattern=".join"))
@Riz20.on(events.NewMessage(pattern=".join"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = rizoel[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("𝐉𝐨𝐢𝐧 𝐇𝐨𝐠𝐲𝐚 𝐒𝐢𝐫")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



@Riz.on(events.NewMessage(pattern=".pjoin"))
@Riz2.on(events.NewMessage(pattern=".pjoin"))
@Riz3.on(events.NewMessage(pattern=".pjoin"))
@Riz4.on(events.NewMessage(pattern=".pjoin"))
@Riz5.on(events.NewMessage(pattern=".pjoin"))
@Riz6.on(events.NewMessage(pattern=".pjoin"))
@Riz7.on(events.NewMessage(pattern=".pjoin"))
@Riz8.on(events.NewMessage(pattern=".pjoin"))
@Riz9.on(events.NewMessage(pattern=".pjoin"))
@Riz10.on(events.NewMessage(pattern=".pjoin"))
@Riz11.on(events.NewMessage(pattern=".pjoin"))
@Riz12.on(events.NewMessage(pattern=".pjoin"))
@Riz13.on(events.NewMessage(pattern=".pjoin"))
@Riz14.on(events.NewMessage(pattern=".pjoin"))
@Riz15.on(events.NewMessage(pattern=".pjoin"))
@Riz16.on(events.NewMessage(pattern=".pjoin"))
@Riz17.on(events.NewMessage(pattern=".pjoin"))
@Riz18.on(events.NewMessage(pattern=".pjoin"))
@Riz19.on(events.NewMessage(pattern=".pjoin"))
@Riz20.on(events.NewMessage(pattern=".pjoin"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/abcdefghijklmsnob\n\n.pjoin abcdefghijklmsnob"
    if e.sender_id in SMEX_USERS:
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = rizoel[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("𝐉𝐨𝐢𝐧 𝐇𝐨𝐠𝐲𝐚 𝐒𝐢𝐫")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
