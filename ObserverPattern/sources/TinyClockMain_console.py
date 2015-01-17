#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
@brief  TinyClock console版.
"""

import threading
import time         #time.sleep()を使用する為.

from View.TinyClockView import TinyClockView
from Model.TinyClockModel import TinyClockModel

def refresh_view(i_View):
    """
    @brief  Viewのリフレッシュ.
            時刻を表示する.
            時計表示スレッドから呼ばれる.
    """
    while 1:
        #1秒スリープ.
        time.sleep(1.0)
        theThreadName = threading.currentThread().getName()
        print("%s \t %s")%(theThreadName, i_View.get_time())


def main():
    """
    @brief  TinyClock console版 main処理
    @note   以下を別スレッドを生成して時刻を表示する.
                アナログ時計
                デジタル時計
            スリープを使用してスレッドを切り替えている為, 
            スレッドの同期はとっていない.
    """
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
        #1秒スリープ.
        time.sleep(1.0)

if __name__=='__main__':
	main()

