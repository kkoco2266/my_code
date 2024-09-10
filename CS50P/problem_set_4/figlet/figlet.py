from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fnts = figlet.getFonts()

if len(sys.argv) != 1 and len(sys.argv) != 3 :
    sys.exit('Invalid Usage')
elif len(sys.argv) == 3 and not (sys.argv[1] in ['-f', '-font']) :
    sys.exit('Invalid Usage')
elif len(sys.argv) == 3 and not (sys.argv[2] in fnts) :
    sys.exit('Invalid Usage')

if len(sys.argv) == 1 :
    font_choice = random.choice(fnts)
else:
    font_choice = sys.argv[2]

figlet.setFont(font=font_choice)

words = input('Input: ')
print(figlet.renderText(words))
