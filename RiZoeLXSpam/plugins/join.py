import asyncio
from .. import Riz, Riz2, Riz3, Riz4, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20, SUDO_USERS
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon import events
import os
import random
import sys


@Riz.on(events.NewMessage(pattern=r"\.join"))
@Riz2.on(events.NewMessage(pattern=r"\.join"))
@Riz3.on(events.NewMessage(pattern=r"\.join"))
@Riz4.on(events.NewMessage(pattern=r"\.join"))
@Riz5.on(events.NewMessage(pattern=r"\.join"))
@Riz6.on(events.NewMessage(pattern=r"\.join"))
@Riz7.on(events.NewMessage(pattern=r"\.join"))
@Riz8.on(events.NewMessage(pattern=r"\.join"))
@Riz9.on(events.NewMessage(pattern=r"\.join"))
@Riz10.on(events.NewMessage(pattern=r"\.join")) 
@Riz11.on(events.NewMessage(pattern=r"\.join")) 
@Riz12.on(events.NewMessage(pattern=r"\.join")) 
@Riz13.on(events.NewMessage(pattern=r"\.join")) 
@Riz14.on(events.NewMessage(pattern=r"\.join")) 
@Riz15.on(events.NewMessage(pattern=r"\.join"))
@Riz16.on(events.NewMessage(pattern=r"\.join"))
@Riz17.on(events.NewMessage(pattern=r"\.join"))
@Riz18.on(events.NewMessage(pattern=r"\.join"))
@Riz19.on(events.NewMessage(pattern=r"\.join"))
@Riz20.on(events.NewMessage(pattern=r"\.join"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SUDO_USERS:
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



@Riz.on(events.NewMessage(pattern=r"\.pjoin"))
@Riz2.on(events.NewMessage(pattern=r"\.pjoin"))
@Riz3.on(events.NewMessage(pattern=r"\.pjoin"))
@Riz4.on(events.NewMessage(pattern=r"\.pjoin"))
@Riz5.on(events.NewMessage(pattern=r"\.pjoin"))
@Riz6.on(events.NewMessage(pattern=r"\.pjoin"))
@Riz7.on(events.NewMessage(pattern=r"\.pjoin"))
@Riz8.on(events.NewMessage(pattern=r"\.pjoin"))
@Riz9.on(events.NewMessage(pattern=r"\.pjoin"))
@Riz10.on(events.NewMessage(pattern=r"\.pjoin"))
@Riz11.on(events.NewMessage(pattern=r"\.pjoin"))
@Riz12.on(events.NewMessage(pattern=r"\.pjoin"))
@Riz13.on(events.NewMessage(pattern=r"\.pjoin"))
@Riz14.on(events.NewMessage(pattern=r"\.pjoin"))
@Riz15.on(events.NewMessage(pattern=r"\.pjoin"))
@Riz16.on(events.NewMessage(pattern=r"\.pjoin"))
@Riz17.on(events.NewMessage(pattern=r"\.pjoin")) 
@Riz18.on(events.NewMessage(pattern=r"\.pjoin"))
@Riz19.on(events.NewMessage(pattern=r"\.pjoin"))
@Riz20.on(events.NewMessage(pattern=r"\.pjoin"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/abcdefghijklmsnob\n\n.pjoin abcdefghijklmsnob"
    if e.sender_id in SUDO_USERS:
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
