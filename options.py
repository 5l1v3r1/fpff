import time,sys,random,os
from colorama import *
r = Fore.RED
g = Fore.GREEN
w = Fore.WHITE
b = Fore.BLUE
y = Fore.YELLOW
m = Fore.MAGENTA
res = Style.RESET_ALL

def clear():
    l = 'clear'
    w = 'cls'
    os.system([l,w][os.name == 'nt'])

def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """

            __________  ____________                        __          __
           / ____/ __ \/ ____/ ____/  ____  _________      / /__  _____/ /_
          / /_  / /_/ / /_  / /_     / __ \/ ___/ __ \__  / / _ \/ ___/ __/
         / __/ / ____/ __/ / __/    / /_/ / /  / /_/ / /_/ /  __/ /__/ /_
        /_/   /_/   /_/   /_/      / .___/_/   \____/\____/\___/\___/\__/
                                  /_/     Fake Page File Founder v1.0

                iranaincoders.ir - github.com/iwhh




    """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" %(random.choice(colors), line, clear))
        time.sleep(0.05)
