#! /usr/bin/python
# -*- coding: utf-8 -*-

import threading
import time

from View.TinyClockView import TinyClockView
from Model.TinyClockModel import TinyClockModel

def refresh_view(i_View):
    while 1:
        time.sleep(1.0)
        theThreadName = threading.currentThread().getName()
        print("%s \t %02d-%02d-%02d %02d:%02d:%02d")%(theThreadName, i_View.year, i_View.month, i_View.day, i_View.hour, i_View.min, i_View.sec)


def main():
    #時計本体部を生成.
    theModel = TinyClockModel()
    #アナログ時計表示部を生成.
    theAnalogClockView = TinyClockView()
    #デジタル時計表示部を生成.
    theDigitalClockView = TinyClockView()

    #時計 本体部と表示部接続.
    theModel.attach(theAnalogClockView)
    theModel.attach(theDigitalClockView)

    #アナログ時計表示部のスレッドを生成.
    theAnalogClockViewThread= threading.Thread(target=refresh_view, name="AnalogClock", args=[theAnalogClockView])
    theAnalogClockViewThread.setDaemon(True)
    theAnalogClockViewThread.start()

    #デジタル時計表示部のスレッドを生成.
    theDigitalClockViewThread = threading.Thread(target=refresh_view, name="DigitalClock", args=[theDigitalClockView])
    theDigitalClockViewThread.setDaemon(True)
    theDigitalClockViewThread.start()


    while 1:
        theModel.set_time()
        time.sleep(1.0)

if __name__=='__main__':
	main()

