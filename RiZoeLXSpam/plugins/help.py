import asyncio
import os
from telethon import events
from telethon import functions, types
from RiZoeLXSpam import (
  Riz, 
  Riz2, 
  Riz3, 
  Riz4, 
  Riz5, 
  Riz6, 
  Riz7, 
  Riz8, 
  Riz9, 
  Riz10, 
  Riz11, 
  Riz12, 
  Riz13, 
  Riz14, 
  Riz15, 
  Riz16, 
  Riz17, 
  Riz18, 
  Riz19, 
  Riz20, 
  Riz21, 
  Riz22, 
  Riz23, 
  Riz24, 
  Riz25, 
  Riz26, 
  Riz27, 
  Riz28, 
  Riz29, 
  Riz30, 
  Riz31, 
  Riz32, 
  Riz33, 
  Riz34, 
  Riz35, 
  Riz36, 
  Riz37, 
  Riz38, 
  Riz39, 
  Riz40,
  DEV, 
  OWNER_ID, 
  SUDO_USERS,
)
from .. import CMD_HNDLR as hl



@Riz.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz11.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz12.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz13.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz14.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz15.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz16.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz17.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz18.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz19.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz20.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz21.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz22.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz23.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz24.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz25.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz26.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz27.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz28.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz29.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz30.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz31.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz32.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz33.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz34.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz35.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz36.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz37.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz38.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz39.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Riz40.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def bot_help(e):
    if e.sender_id in SUDO_USERS or e.sender_id in DEV:
        RiZoeL = e.text.split(" ")
        if len(RiZoeL) > 1:
            helping = RiZoeL[1]
            if helping.lower() == "spam":
                await e.reply(spam_help)
            elif helping.lower() == "raid":
                await e.reply(raid_help)
            elif helping.lower() == "dm":
                await e.reply(dm_help)
            elif helping.lower() == "echo":
                await e.reply(echo_help)
            elif helping.lower() == "userbot":
                await e.reply(userbot_help)
            elif helping.lower() == "join":
                await e.reply(join_help)
            elif helping.lower() == "leave":
                await e.reply(leave_help)
            elif helping.lower() == "extra":
                await e.reply(extra_help)
            elif helping.lower() == "owner":
                await e.reply(owner_help)
            else:
                await e.reply(help_menu)
        else:
            await e.reply(help_menu)


spam_help = f"""
**• Spam Cmds •**

**spam**: Spams a message for given counter(<= 100).
commands:
i) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}spam <count> <replying any message>

**bigspam**: Spams a message for given counter.
commands:
i) {hl}bigspam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}bigspam <count> <replying any message>

**delayspam**: Delay spam a text for given counter after given time.
commands:
i) {hl}delayspam <delay time(seconds)> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}delayspam <delay time(seconds)> <count> <replying any message>

**pornspam**: Spams hanging message for given counter.
commands:
i) {hl}pornspam <counter>

**packspam**: Spams all stickers from sticker pack.
commands: 
i) {hl}packspam (replying to any sticker)

**hang**: Spams hanging message for given counter.
commands:
i) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)

**© @RiZoeLX**
"""


raid_help = f"""
**• Raid Cmds •**

**raid:** Activates raid on any individual user for given range.
commands:
i) {hl}raid <count> <username>
ii) {hl}raid <count> <reply to the user>

**Delayraid**: Activates raid on any individual user for given range.
Command:
i) {hl}delayraid <delay> <count> <Username of User>
ii) {hl}delayraid <delay> <count> <reply to a User>

**replyraid:** Activates reply raid on individual user
commands:
i) {hl}replyraid <replying to anyone>
ii) {hl}replyraid <username>

**dreplyraid:** De-activates reply raid from user!!
commands:
i) {hl}dreplyraid <replying to anyone>
ii) {hl}dreplyraid <username>


**© @RiZoeLX**
"""


dm_help = f"""
**• Dm Cmds •**

**Dm:** Dm to any individual using spam bots
command:
i) {hl}dm <username> <message>
ii) {hl}dm <message> <reply to the user>

**Dm Spam:** Spam in Dm of Any individual Users
command:
i) {hl}dmspam <count> <username> <message to spam>
ii) {hl}dmspam <count> <username> <reply to a message>

**Dm Raid:** raid in Dm of Any individual Users
command:
i) {hl}dmraid <count> <username>
ii) {hl}dmraid <count> <reply to the user>

**© @RiZoeLX**
"""

echo_help = f"""
**• Echo cmds •**

**addecho:** Active Echo On user
Command:
{hl}addecho <reply to user>

**rmecho:** De-activate Echo From user
Command:
{hl}rmecho <reply to user>

**© @RiZoeLX**
"""

join_help = f"""
**• Join Cmds •**

**join:** Join any Public Channel and group
command:
{hl}join <channel/group invite link or username>

**pjoin:** Join Any Private Channel Or group
command:
{hl}pjoin <channel/group Hash>

Example: group Link : https://t.me/+Abcdefghijkl
cmd : {hl}pjoin Abcdefghijkl

__Only Owner And Full Sudo Users can !!__

**© @RiZoeLX
"""

leave_help = f"""
**• Leave Cmds •**

**leave:** Leave any Public/private Group or Channel
commands:
i) {hl}leave <group or channel chat id>
ii) {hl}leave

__Only Owner And Full Sudo Users can !!__

**© @RiZoeLX**
"""

userbot_help = f"""
**• Userbot Cmds •**

**Commands:**

- {hl}ping : To check Ping 

- {hl}alive : To check Bot Version and Other info

- {hl}restart : To Restart Your Spam Bots

**© @RiZoeLX**
"""

extra_help = f"""
**• Extra Cmds •**

**abuse:** Abuse Any Individual user continuously
command:
{hl}abuse <username>

__we'll Add More Cmds Soon__

**© @RiZoeLX**
"""

owner_help = f"""
**• Owner And Full Sudo Cmds •**
__Note__ : Only Spam Bot's Owner and Full Sudo Can Use this cmds.

**Inviteall:** Mass adding In Group
command:
{hl}inviteall <Public Group invite Link or username>

**Profile:** Profile And Other Cmds
commands:

1) {hl}setname <Profile Name>
2) {hl}setbio <coustom Bio>
3) {hl}stats

**Add Sudo:** Add Sudo Using Spam bots
commands:
1) {hl}addsudo <reply to user>
2) {hl}fullsudo <reply to user>
"""

help_menu = f"""
**RiZoeL X Spam Help**

**There are following categories**

`owner` : Get all owner and Full Sudo commands and its usage
`spam` : Get all spam commands and its usage
`raid` : Get all raid commands and its usage
`dm` : Get all dm commands and its usage
`echo` : Get echo commands and its usage
`join` : Get join commands and its usage
`leave` : Get leave commands and its usage
`userbot` : Get all userbot commands
`extra` : Get all extra commands and its usage

**Type** {hl}help <category> **to get all commands in that category and its usage**
**Example**: `{hl}help spam`

**© @RiZoeLX**
"""
