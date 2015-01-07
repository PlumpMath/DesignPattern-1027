#! /usr/bin/python
# -*- coding: utf-8 -*-

from Lib.Observer import Observer

#時計表示部（表示データ保持）
class TinyClockView(Observer):
    def __init__(self):
        #スーパークラス初期化.
        Observer.__init__(self)
        #メンバー変数初期化.
        self._year = -1
        self._month = -1
        self._day = -1
        self._hour = -1
        self._min = -1
        self._sec = -1

    @property
    def year(self):     return self._year

    @property
    def month(self):    return self._month

    @property
    def day(self):      return self._day

    @property
    def hour(self):     return self._hour

    @property
    def min(self):      return self._min

    @property
    def sec(self):      return self._sec

    def set_time(self, modifier):
        self._year = modifier.year
        self._month = modifier.month
        self._day = modifier.day
        self._hour = modifier.hour
        self._min = modifier.min
        self._sec = modifier.sec

    def update(self, modifier=None):
        self.set_time(modifier)

##################################################
# テスト関数とメイン関数.
#
##################################################
if __name__ == "__main__":
    class ModelInterfaceMock(object):
        def __init__(self):
            self.year = 2014
            self.month = 12
            self.day = 27
            self.hour = 20
            self.min = 15
            self.sec = 25

    def main():
        theModel = ModelInterfaceMock()
        theView = TinyClockView()
        theView.update(theModel)
        print("%02d-%02d-%02d %02d:%02d:%02d")%(theView.year, theView.month, theView.day, theView.hour, theView.min, theView.sec)

    #メイン.
    main()
