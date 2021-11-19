#RiZoeLXSpam By @TheRiZoeL

import sys
from sys import argv
import glob
from pathlib import Path
from RiZoeLXSpam.utils import load_plugins
import logging
from . import Riz, Riz2, Riz3, Riz4, Riz5, Riz6, Riz7, Riz8, Riz9, Riz10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

async def start_RiZoeLX():
        try:
            await Riz.start()
            botme = await Riz.get_me()
            await Riz(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz(functions.channels.JoinChannelRequest(channel="@DNHxHeLL"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
        try:
            await Riz2.start()
            await Riz2(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz2(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botme = await Riz2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
        try:
            await  Riz3.start()
            await Riz3(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz3(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botme = await Riz3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
        try:
            await Riz5.start()
            await Riz5(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz5(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botme = await Riz5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
        try:
            await Riz4.start()
            await Riz4(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz4(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botme = await Riz4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
        try:
            await Riz6.start()
            await Riz6(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz6(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botme = await Riz6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
        try:
            await Riz7.start()
            await Riz7(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz7(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botme = await Riz7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
        try:
            await Riz8.start()
            await Riz8(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz8(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botme = await Riz8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
        try:
            await Riz9.start()
            await Riz9(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz9(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botme = await Riz9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
        try:
            await Riz10.start()
            await Riz10(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz10(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botme = await Riz10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass

path = "RiZoeLXSpam/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("RiZoeL Bot Spam Successfully deployed -!")
print("Enjoy! Do visit @RiZoeLX")
loop = asyncio.get_event_loop()
loop.run_until_complete(start_RiZoeLX()) 

if len(argv) not in (1, 3, 4):
    try:
        Riz.disconnect()
    except Exception as e:
        pass
    try:
        Riz2.disconnect()
    except Exception as e:
        pass
    try:
        Riz3.disconnect()
    except Exception as e:
        pass
    try:
        Riz4.disconnect()
    except Exception as e:
        pass
    try:
        Riz5.disconnect()
    except Exception as e:
        pass
    try:
        Riz6.disconnect()
    except Exception as e:
        pass
    try:
        Riz7.disconnect()
    except Exception as e:
        pass
    try:
        Riz8.disconnect()
    except Exception as e:
        pass
    try:
        Riz9.disconnect()
    except Exception as e:
        pass
    try:
        Riz10.disconnect()
    except Exception as e:
        pass
else:
    try:
        Riz.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz2.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz3.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz4.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz5.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz6.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz7.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz8.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz9.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Riz10.run_until_disconnected()
    except Exception as e:
        pass
