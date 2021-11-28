
import asyncio
import base64
import os
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl import functions
from telethon.tl.functions.account import UpdateUsernameRequest
from .. import Riz, Riz2, Riz3, Riz4, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20, SUDO_USERS
from telethon import events


@Riz.on(events.NewMessage(pattern=r"\.setname"))
@Riz2.on(events.NewMessage(pattern=r"\.setname"))
@Riz3.on(events.NewMessage(pattern=r"\.setname"))
@Riz4.on(events.NewMessage(pattern=r"\.setname"))
@Riz5.on(events.NewMessage(pattern=r"\.setname"))
@Riz6.on(events.NewMessage(pattern=r"\.setname"))
@Riz7.on(events.NewMessage(pattern=r"\.setname"))
@Riz8.on(events.NewMessage(pattern=r"\.setname"))
@Riz9.on(events.NewMessage(pattern=r"\.setname"))
@Riz10.on(events.NewMessage(pattern=r"\.setname"))
@Riz11.on(events.NewMessage(pattern=r"\.setname"))
@Riz12.on(events.NewMessage(pattern=r"\.setname"))
@Riz13.on(events.NewMessage(pattern=r"\.setname"))
@Riz14.on(events.NewMessage(pattern=r"\.setname"))
@Riz15.on(events.NewMessage(pattern=r"\.setname"))
@Riz16.on(events.NewMessage(pattern=r"\.setname"))
@Riz17.on(events.NewMessage(pattern=r"\.setname"))
@Riz18.on(events.NewMessage(pattern=r"\.setname"))
@Riz19.on(events.NewMessage(pattern=r"\.setname"))
@Riz20.on(events.NewMessage(pattern=r"\.setname"))
async def name(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = SET NAME\n\nCommand:\n\n.setname <Message to change name of spam ids>"
    if e.sender_id in SUDO_USERS:
        names = e.text.split(" ", 1)
        RiZoeL = names[1]
        if len(e.text) > 5:
            firstname = RiZoeL
            text = "Changing Name..."
            try:
                await e.client(functions.account.UpdateProfileRequest(first_name=firstname))
                event = await e.reply(text, parse_mode=None, link_preview=None )
                await event.edit("Changed name successfully!")
            except Exception as e:
                await print(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
