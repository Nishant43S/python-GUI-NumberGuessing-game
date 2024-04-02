import pyautogui as gui
import random
stat = gui.confirm(title="Number guessing game by Nishant Maity",
            text='''
            > choose a number
            > if number = computer number
            > you win
            ''',
            buttons=["start","exit"])
if stat == str("start"):
    x = random.randint(1,100)
    count = 0
    while True:
        count = count+1
        val = gui.prompt("enter any number between (1-100)",
                         title="number guessing game")
        if int(val) > x:
            gui.alert(f"enter smaller number: {val}","use smaller number")
        elif int(val) < x:
            gui.alert(f"enter greater number: {val}","use greater number")
        elif int(val) == x:
            break
    if int(val) == x:
        gui.alert(" You got the number 🎊","\n",
                  f"you have take {count} chances")
else:
    gui.alert("thanks for playing")