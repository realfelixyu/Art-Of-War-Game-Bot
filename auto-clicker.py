import time
import threading
import sys
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import pyautogui


delay = 1.000
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')


class ArtOfWarBot(threading.Thread):


    def __init__(self, button):
        super(ArtOfWarBot, self).__init__()
        self.fight_delay = 15.000
        self.ad_delay = 31.000
        self.button = button
        self.running = False
        self.program_running = True
        self.ad1x = 560
        self.ad1y = 70
        self.ad2x = 36
        self.ad2y = 70
        self.counter = 1
        self.headhuntx1 = 500
        self.headhunty1 = 420
        self.headhuntx2 = self.headhuntx1
        self.headhunty2 = 670

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def getAdButtonPoint(self, imageName):
        self.adButton = pyautogui.locateOnScreen('.\\' + imageName)
        return pyautogui.center(self.adButton)

    #currently not compatible with game
    def closeAds(self, images):
        for i in images:
            point = pyautogui.center(pyautogui.locateOnScreen('.\\' + i))
            mouse.position = (point.x, point.y)
            mouse.click()
            time.sleep(0.01)

    def normalBattle(self):
        mouse.position = self.returnPointFromImage('battlebutton')
        mouse.click(self.button)
        time.sleep(0.3)
        pyautogui.doubleClick()
        mouse.click(self.button)
        time.sleep(0.2)
        pyautogui.doubleClick()
        time.sleep(0.2)
        pyautogui.doubleClick()
        time.sleep(self.fight_delay)
        mouse.position = self.returnPointFromImage('watch-ad-button')
        mouse.click(self.button)
        time.sleep(self.ad_delay)
        self.closeAd()
        self.counter += 1
        time.sleep(1)

    def closeAd(self):
        mouse.position = (self.ad1x, self.ad1y)
        mouse.click(self.button)
        mouse.position = (self.ad2x, self.ad2y)
        mouse.click(self.button)

    def returnPointFromImage(self, imageName):
        for i in range(10):
            time.sleep(0.3)
            try:
                point = pyautogui.center(pyautogui.locateOnScreen('.\\' + imageName + '.png'))
                break
            except:
                print('trying to find' + imageName)
        return (point.x, point.y)

    def headHuntBattle(self):
        # imageName = 'custom-attack-'
        # for i in range(1,11):
        #     try:
        #         point = pyautogui.center(pyautogui.locateOnScreen('.\\' + imageName + str(i) + '.png'))
        #         mouse.position = (point.x, point.y)
        #         mouse.click(self.button)
        #         break
        #     except:
        #         print('cannot find ' + str(i))
        mouse.position = (self.headhuntx1, self.headhuntx2)
        mouse.click(self.button)
        mouse.position = (self.headhuntx2, self.headhunty2)
        mouse.click(self.button)
        time.sleep(1.5)
        for i in range(10):
            try:
                mouse.position = self.returnPointFromImage('custom-fight-button')
                break
            except:
                print('error finding fight button, gonna refind')
                time.sleep(0.5)
        mouse.click(self.button)
        time.sleep(0.5)
        pyautogui.doubleClick()
        time.sleep(10)
        self.watchAd()

    def watchAd(self):
        while (True):
            try:
                mouse.position = self.returnPointFromImage('watch-ad-button')
                mouse.click(self.button)
                break
            except:
                print('trying to find ad button')
        time.sleep(self.ad_delay)
        self.closeAd()
        time.sleep(2)

    def openCardPack(self, count):
        cardPackPoint = pyautogui.center(pyautogui.locateOnScreen('.\\card-pack.png'))
        mouse.position = (cardPackPoint.x, cardPackPoint.y)
        mouse.click(self.button)
        time.sleep(0.5)
        cardPackConfirmPoint = pyautogui.center(pyautogui.locateOnScreen('.\\card-pack-confirm.png'))
        mouse.position = (cardPackConfirmPoint.x, cardPackConfirmPoint.y)
        mouse.click(self.button)
        time.sleep(2.5)
        anotherCardpack = pyautogui.center(pyautogui.locateOnScreen('.\\another-card-pack.png'))
        mouse.position = (anotherCardpack.x, anotherCardpack.y)
        mouse.click(self.button)
        for i in range(count - 1):
            time.sleep(1.5)
            mouse.click(self.button)

    def run(self):
        while self.program_running:
            while self.running:
                self.normalBattle()
                #self.openCardPack(10)
                #self.headHuntBattle()
                print(self.counter)
                self.counter += 1
            time.sleep(0.1)


mouse = Controller()
click_thread = ArtOfWarBot(button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()
        sys.exit()

with Listener(on_press=on_press) as listener:
    listener.join()

'''     main_x = 700
        main_y = 750
        ad_x = 650
        ad_y = 600
        close_ad_x1 = 980
        close_ad_y1 = 70
        close_ad_x2 = 560
        close_ad_y2 = 70
        '''
