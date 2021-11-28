from .. import Riz, Riz2, Riz3, Riz4, Riz5, Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20, SUDO_USERS
from telethon import events
import os
import random
import sys


@Riz.on(events.NewMessage(pattern=r"\.restart"))
@Riz2.on(events.NewMessage(pattern=r"\.restart"))
@Riz3.on(events.NewMessage(pattern=r"\.restart"))
@Riz4.on(events.NewMessage(pattern=r"\.restart"))
@Riz5.on(events.NewMessage(pattern=r"\.restart"))
@Riz6.on(events.NewMessage(pattern=r"\.restart"))
@Riz7.on(events.NewMessage(pattern=r"\.restart"))
@Riz8.on(events.NewMessage(pattern=r"\.restart"))
@Riz9.on(events.NewMessage(pattern=r"\.restart"))
@Riz10.on(events.NewMessage(pattern=r"\.restart"))
@Riz11.on(events.NewMessage(pattern=r"\.restart"))
@Riz12.on(events.NewMessage(pattern=r"\.restart"))
@Riz13.on(events.NewMessage(pattern=r"\.restart"))
@Riz14.on(events.NewMessage(pattern=r"\.restart"))
@Riz15.on(events.NewMessage(pattern=r"\.restart"))
@Riz16.on(events.NewMessage(pattern=r"\.restart"))
@Riz17.on(events.NewMessage(pattern=r"\.restart"))
@Riz18.on(events.NewMessage(pattern=r"\.restart"))
@Riz19.on(events.NewMessage(pattern=r"\.restart"))
@Riz20.on(events.NewMessage(pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "**Restarting Your RiZoeL X Spam**.. Please Wait Until It Starts Again"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await Riz.disconnect()
        except Exception:
            pass
        try:
            await Riz2.disconnect()
        except Exception:
            pass
        try:
            await Riz3.disconnect()
        except Exception:
            pass
        try:
            await Riz4.disconnect()
        except Exception:
            pass
        try:
            await Riz5.disconnect()
        except Exception:
            pass
        try:
            await Riz6.disconnect()
        except Exception:
            pass
        try:
            await Riz7.disconnect()
        except Exception:
            pass
        try:
            await Riz8.disconnect()
        except Exception:
            pass
        try:
            await Riz9.disconnect()
        except Exception:
            pass
        try:
            await Riz10.disconnect()
        except Exception:
            pass
        try:
            await Riz11.disconnect()
        except Exception:
            pass
        try:
            await Riz12.disconnect()
        except Exception:
            pass
        try:
            await Riz13.disconnect()
        except Exception:
            pass
        try:
            await Riz14.disconnect()
        except Exception:
            pass
        try:
            await Riz15.disconnect()
        except Exception:
            pass
        try:
            await Riz16.disconnect()
        except Exception:
            pass
        try:
            await Riz17.disconnect()
        except Exception:
            pass
        try:
            await Riz18.disconnect()
        except Exception:
            pass
        try:
            await Riz19.disconnect()
        except Exception:
            pass
        try:
            await Riz20.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
