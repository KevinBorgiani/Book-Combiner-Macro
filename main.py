import pyautogui as bot
import keyboard as kb
import time

time.sleep(3)
bot.PAUSE = 0.33

anvil = (676, 275)

slots = [
    (534, 442), (570, 449), (605, 444), (642, 446),
    (675, 446), (710, 446), (745, 446), (534, 477),
    (570, 477), (605, 477), (642, 477), (675, 477),
    (710, 477), (745, 477), (534, 512), (570, 512)
]

bot.press('enter')
kb.write("/av")
bot.press('enter')

time.sleep(1)

fodase = 1
while fodase <= 8:
    for i in range(0, len(slots) // fodase, 2):
        bot.moveTo(slots[i])
        bot.keyDown('shift')
        bot.click()
        
        if i + 1 < len(slots):
            bot.moveTo(slots[i + 1])
            bot.click()
        
        bot.keyUp('shift')
        
        bot.moveTo(anvil)
        bot.click()
        bot.click()
    
    fodase *= 2  

bot.hotkey('esc')
bot.hotkey('enter')
bot.write("/bz")
bot.hotkey('enter')

bot.moveTo(534, 442)
bot.click()

bot.moveTo(789, 273)
bot.click()

bot.moveTo(647, 276)
bot.click()

bot.moveTo(685, 274)
bot.click()
