import pyautogui,time

wh=pyautogui.size()
print(wh)

tt=pyautogui.locateOnScreen("C:\\Users\\Vlad\\Desktop\\paint.png")
print(tt)

# while 1<3 :
#     print(pyautogui.position())
#     time.sleep(0.5)


iden1,iden2,iden3,iden4=608,327,627,808,



# for drawing a nice shape
pyautogui.click(1312,1053,duration=1)
#pyautogui.click(tt,duration=1)
time.sleep(1)

pyautogui.click(346,104,duration=1)

for i in range(10):
    pyautogui.moveTo(iden1+i*10,iden2+i*10)#,duration=0.5)
    pyautogui.dragTo(iden1+i*10,iden3-i*10)#,duration=0.5)
    pyautogui.dragTo(iden4-i*10,iden3-i*10)#,duration=0.5)
    pyautogui.dragTo(iden4-i*10,iden2+i*10)#,duration=0.5)
    pyautogui.dragTo(iden1+i*10,iden2+i*10)#,duration=0.5)




# pyautogui.click(100,200,duration=1)
# time.sleep(2)
# pyautogui.write("hai sa vedem ce face",0.26)

# pyautogui.keyDown('ctrl')
# pyautogui.keyDown('shift')
# pyautogui.keyDown('esc')
# while 1<3 :
#      print(pyautogui.position())
#      time.sleep(0.5)

# pyautogui.moveTo(-1648,494,duration=1)
#
# for i in range(200):
#     pyautogui.click()
