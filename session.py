from telethon.sessions import StringSession
from telethon.sync import TelegramClient


print(
    """┏━━┓━━┏━━━┓━━━━━━━━┏┓━\n┃┏┓┃┏┓┃┏━┓┃━━━━━━━━┃┃━\n┃┗┛┃┗┛┗┛━┛┃┏━━┓┏━━┓┃┃━\n┃━━┛┏┓┃┏━┏┓┃┏┓┃┃┏┓┃┃┃━\n┃┃┃┃┃┃┃┗━┛┃┃┗┛┃┃┃━┫┃┗━┓\n┗┛┗┛┗┛┗━━━┛┗━━┛┗━━┛┗━━┛"""
)

print("\n • Telethon Session •")

print("\n\nEnter Your Valid Details To Continue!\n\n")

        
APP_ID = int(input("\nEnter APP ID here: "))
API_HASH = input("\nEnter API HASH here: ")


try:
   with TelegramClient(StringSession(), APP_ID, API_HASH) as RcR:
       print("\nSTRING SESSION GENERATE SUCCESSFULLY CHECK SAVED MASSAGE")
       RcR.send_message("me", f"**RcR X Spam Session :**\n\n`{RcR.session.save()}`\n\n__Do not share this anywhere!!__")
       
except Exception as e:
    print(f"{e}") 
