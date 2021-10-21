#RiZoeLXSpam By @TheRiZoeL
import glob
from pathlib import Path
from RiZoeLXSpam.utils import load_plugins
import logging
from . import Riz, Riz2, Riz3, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, Riz11, Riz12, Riz13, Riz14, Riz15, Riz16, Riz17, Riz18, Riz19, Riz20

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "RiZoeLXSpam/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("RiZoeL Bot Spam Successfully deployed -!")
print("Enjoy! Do visit @RiZoeLX")

if __name__ == "__main__":
    Riz.run_until_disconnected()
    
if __name__ == "__main__":
    Riz2.run_until_disconnected()

if __name__ == "__main__":
    Riz3.run_until_disconnected()
    
if __name__ == "__main__":
    Riz4.run_until_disconnected()

if __name__ == "__main__":
    Riz5.run_until_disconnected()
    
if __name__ == "__main__":
    Riz6.run_until_disconnected()

if __name__ == "__main__":
    Riz7.run_until_disconnected()
    
if __name__ == "__main__":
    Riz8.run_until_disconnected()

if __name__ == "__main__":
    Riz9.run_until_disconnected()
    
if __name__ == "__main__":
    Riz10.run_until_disconnected()

if __name__ == "__main__":
    Riz11.run_until_disconnected()

if __name__ == "__main__":
    Riz12.run_until_disconnected()
    
if __name__ == "__main__":
    Riz13.run_until_disconnected()
    
if __name__ == "__main__":
    Riz14.run_until_disconnected()
    
if __name__ == "__main__":
    Riz15.run_until_disconnected()
   
if __name__ == "__main__":
    Riz16.run_until_disconnected()

if __name__ == "__main__":
    Riz17.run_until_disconnected()

if __name__ == "__main__":
    Riz18.run_until_disconnected()

if __name__ == "__main__":
    Riz19.run_until_disconnected()

if __name__ == "__main__":
    Riz20.run_until_disconnected()
