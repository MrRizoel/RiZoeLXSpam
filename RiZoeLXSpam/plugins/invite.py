import os
import sys
import random
from os import execl
import asyncio
import telethon.utils
from .. import Riz, Riz2, Riz3, Riz4, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20, SUDO_USERS
from telethon.tl import functions
from telethon import events


from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.reply(
                "`This is a private channel/group or I am banned from there`"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Invalid channel/group`")
            return None
    return chat_info


def make_mention(user):
    if user.username:
        return f"@{user.username}"
    else:
        return inline_mention(user)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = " ".join(names)
    return full_name


            
@Riz.on(events.NewMessage(pattern=r"\.inviteall"))
@Riz2.on(events.NewMessage(pattern=r"\.inviteall"))
@Riz3.on(events.NewMessage(pattern=r"\.inviteall"))
@Riz4.on(events.NewMessage(pattern=r"\.inviteall"))
@Riz5.on(events.NewMessage(pattern=r"\.inviteall"))
@Riz6.on(events.NewMessage(pattern=r"\.inviteall"))
@Riz7.on(events.NewMessage(pattern=r"\.inviteall"))
@Riz8.on(events.NewMessage(pattern=r"\.inviteall"))
@Riz9.on(events.NewMessage(pattern=r"\.inviteall"))
@Riz10.on(events.NewMessage(pattern=r"\.inviteall"))
@Riz11.on(events.NewMessage(pattern=r"\.inviteall"))
@Riz12.on(events.NewMessage(pattern=r"\.inviteall"))
@Riz13.on(events.NewMessage(pattern=r"\.inviteall"))
@Riz14.on(events.NewMessage(pattern=r"\.inviteall"))
@Riz15.on(events.NewMessage(pattern=r"\.inviteall"))
@Riz16.on(events.NewMessage(pattern=r"\.inviteall"))
@Riz17.on(events.NewMessage(pattern=r"\.inviteall"))
@Riz18.on(events.NewMessage(pattern=r"\.inviteall"))
@Riz19.on(events.NewMessage(pattern=r"\.inviteall"))
@Riz20.on(events.NewMessage(pattern=r"\.inviteall"))
async def get_users(event):
    if event.sender_id in SUDO_USERS:
        rkp = await event.reply("`processing...`")
    else:
        rkp = await event.edit("`processing...`")
    rk1 = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await rkp.edit("`Sorry, Can add users here`")
    s = 0
    f = 0
    error = "None"

    await rkp.edit("**TerminalStatus**\n\n`Collecting Users.......`")
    async for user in event.client.iter_participants(rk1.full_chat.id):
        try:
            if error.startswith("Too"):
                return await rkp.edit(
                    f"**Terminal Finished With Error**\n(`May Got Limit Error from telethon Please try agin Later`)\n**Error** : \n`{error}`\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people"
                )
            await event.client(
                functions.channels.InviteToChannelRequest(channel=chat, users=[user.id])
            )
            s = s + 1
            await rkp.edit(
                f"**Terminal Running...**\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people\n\n**× LastError:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await rkp.edit(
        f"**Terminal Finished** \n\n• Successfully Invited `{s}` people \n• failed to invite `{f}` people"
    )        
