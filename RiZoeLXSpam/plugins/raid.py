
import asyncio
import base64
import os
import random
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import Riz, Riz2, Riz3, Riz4, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20, RAID, RRAID, SUDO_USERS

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

que = {}
RiZoeLX = [1517994352, 2086101519]


@Riz.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."  
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Rizoel) == 2:
            message = str(Rizoel[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            if int(g) in RiZoeLX:
                text = f"LOL. I can't raid on @RiZoeLX's Owne"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SMEX_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(Rizoel[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in RiZoeLX:
                text = f"I can't raid on @RiZoeLX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SMEX_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
            c = b.first_name
            counter = int(Rizoel[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



@Riz.on(events.NewMessage(incoming=True))
@Riz2.on(events.NewMessage(incoming=True))
@Riz3.on(events.NewMessage(incoming=True))
@Riz4.on(events.NewMessage(incoming=True))
@Riz5.on(events.NewMessage(incoming=True))
@Riz6.on(events.NewMessage(incoming=True))
@Riz7.on(events.NewMessage(incoming=True))
@Riz8.on(events.NewMessage(incoming=True))
@Riz9.on(events.NewMessage(incoming=True))
@Riz10.on(events.NewMessage(incoming=True))
@Riz11.on(events.NewMessage(incoming=True))
@Riz12.on(events.NewMessage(incoming=True))
@Riz13.on(events.NewMessage(incoming=True))
@Riz14.on(events.NewMessage(incoming=True))
@Riz15.on(events.NewMessage(incoming=True))
@Riz16.on(events.NewMessage(incoming=True))
@Riz17.on(events.NewMessage(incoming=True))
@Riz18.on(events.NewMessage(incoming=True))
@Riz19.on(events.NewMessage(incoming=True))
@Riz20.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )


@Riz.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>"
    global que
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(e.text) > 11:
            message = str(Rizoel[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            if int(g) in RiZoeLX:
                text = f"I can't raid on @RiZoeLX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SMEX_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None)
        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            if int(g) in RiZoeLX:
                text = f"I can't raid on @RiZoeLX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SMEX_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@Riz.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    global que    
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(Rizoel[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
