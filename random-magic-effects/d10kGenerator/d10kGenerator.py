import string
import random 
import createList
import pyperclip

Rolls = createList.Effects()

while True:
    rollIndex = random.randint(0,len(Rolls) - 1)
    print(Rolls[rollIndex])

    pyperclip.copy(Rolls[rollIndex])
    pyperclip.paste()

    if len(input())!=0: break