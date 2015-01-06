#! /usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from Lib.Observer import Subject

class TinyClockModel(Subject):
    def __init__(self):
        Subject.__init__(self)
        self._now = None

    @property
    def year(self):
        theString = self._now.strftime("%Y")
        return int(theString)

    @property
    def month(self):
        theString = self._now.strftime("%m")
        return int(theString)

    @property
    def day(self):
        theString = self._now.strftime("%d")
        return int(theString)
    
    @property
    def hour(self):
        theString = self._now.strftime("%H")
        return int(theString)
    
    @property
    def min(self):
        theString = self._now.strftime("%M")
        return int(theString)

    @property
    def sec(self):
        theString = self._now.strftime("%S")
        return int(theString)

    def set_time(self):
        self._now = datetime.datetime.today()
        self.notify(self)


##################################################
# テスト関数とメイン関数.
#
##################################################
if __name__ == "__main__":
    def main():
        theModel = TinyClockModel()
        theModel.set_time()
        print("%04d-%02d-%02d %02d:%02d:%02d")%(theModel.year, theModel.month, theModel.day, theModel.hour, theModel.min, theModel.sec)

    #メイン.
    main()
