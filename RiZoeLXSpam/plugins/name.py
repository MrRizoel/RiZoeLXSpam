
import asyncio
import base64
import os
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl import functions
from telethon.tl.functions.account import UpdateUsernameRequest
from .. import Riz, Riz2, Riz3, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20, SUDO_USERS

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)


@Riz.on(events.NewMessage(pattern=".setname"))
@Riz2.on(events.NewMessage(pattern=".setname"))
@Riz3.on(events.NewMessage(pattern=".setname"))
@Riz4.on(events.NewMessage(pattern=".setname"))
@Riz5.on(events.NewMessage(pattern=".setname"))
@Riz6.on(events.NewMessage(pattern=".setname"))
@Riz7.on(events.NewMessage(pattern=".setname"))
@Riz8.on(events.NewMessage(pattern=".setname"))
@Riz9.on(events.NewMessage(pattern=".setname"))
@Riz10.on(events.NewMessage(pattern=".setname"))
@Riz11.on(events.NewMessage(pattern=".setname"))
@Riz12.on(events.NewMessage(pattern=".setname"))
@Riz13.on(events.NewMessage(pattern=".setname"))
@Riz14.on(events.NewMessage(pattern=".setname"))
@Riz15.on(events.NewMessage(pattern=".setname"))
@Riz16.on(events.NewMessage(pattern=".setname"))
@Riz17.on(events.NewMessage(pattern=".setname"))
@Riz18.on(events.NewMessage(pattern=".setname"))
@Riz19.on(events.NewMessage(pattern=".setname"))
@Riz20.on(events.NewMessage(pattern=".setname"))
async def _(event):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = SET NAME\n\nCommand:\n\n.setname <Message to change name of spam ids>"
    if e.sender_id in SMEX_USERS:
        return
    names = event.pattern_match.group(1)
    first_name = names
    last_name = ""
    if "|" in names:
        first_name, last_name = names.split("|", 1)
    try:
        await bot(
            functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                first_name=first_name, last_name=last_name
            )
        )
        await event.edit("Name was changed successfully")
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))
