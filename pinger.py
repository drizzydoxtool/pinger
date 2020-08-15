import os, random
from pythonping import ping
swastika = r"""
    _--_
   /    \
  (  **  )
   \    /
    |  |    ........_           ____,,,..---
    |  |^^*|MMMMMMMMM```-----'''MMMMMMMMMMMM|
    |  |   |MMMMMMMMMOMMMMMMMMMM@MMMMMMMMMMM|
    |  |   |MMMMMMMMMOMMMMMMMMMM@MMMMMMMMMMM|
    |  |   |MMMMMMMMMOMMMMMMMMMM@MMMMMMMMMMM|,
    |  |   `|IIIIIIIII+IIYYYYYIII%IIIIIIIIIII|
    |  |    |IIIIIIIII+IIIIIIIIII%IIIIIIIIIII|
    |  |    |IIIIIIIII+IIIIIIIIII%IIIIIIIIIII|,
    |  |    `|IIIIIIIII+IIIIIIIIII%IIIIIIIIIII|
    |  |     |:::::::::"::YYYYY::::=::::::::::|
    |  |    ,|:::::::::":::::::::::=::::::::::|
    |  |    |:::::::::":::::::::::=:::::::::::|'
    |  |'^^*|;;;;;;;;_";:::::::::;=------;;;;;/
    |  |               ```-----'''
    |  |
    |  |
    |  |
    |  |
    |  |
    |  |
    |  |
    |  |
    |  |
    |  |
    |  |
    |  |
    |  |
    |  |
    |  |
    |  |   Q: WHY IS MAKING FUN OF GERMANS SO FUNNY
    |  |
    |  |   A: OPEN YOUR HISTORY BOOK FUCKFACE
    |  |
  \\|  |//
''''''''''''''''''~~~~~~~~~~~~~~~~~~
"""
os.system("title 卐 SEIG HEIL 卐")
superlongvariablename = ['a','b','c','d','e','0','1','2','3','4','5','6','7','8','9']
os.system("cls")
ip = input("Enter the victim's IP: ")
slurs = ['PORCHMONKEY', 'APE', 'NIGGER', 'BABOON', 'KIDDIE FIDLER', 'KNUCKLE DRAGGER']
print(swastika)
while True:
    x = str(ping(ip, count=1, verbose=False, timeout=69420911))
    colorbutwithlongernamebecausecoloristakenalready = random.choice(superlongvariablename)
    os.system(f"color {colorbutwithlongernamebecausecoloristakenalready}")
    if x.startswith("Reply from"):
        print(f"{ip} ONLINE")
    elif "transmit failed" in "x":
        print(f"{ip} is an invalid IP.")
        break
    else:
        print(f"ERROR: HEIL HITLER. {random.choice(slurs)} OFFLINE.")
