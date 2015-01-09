#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
@brief  時計本体部.
"""

import datetime
from Lib.Observer import Subject

class TinyClockModel(Subject):
    """
    @brief  時計本体部 クラス.
    @note   Subjectクラスを継承.
            時刻を取得し, 表示部へ通知する.
    """

    def __init__(self):
        """
        @brief  初期化.
        @param  メンバー変数    self._now   現在時刻.
        """
        Subject.__init__(self)
        self._now = None

    @property
    def year(self):
        """
        @return 現在 年.
        """
        theString = self._now.strftime("%Y")
        return int(theString)

    @property
    def month(self):
        """
        @return 現在 月.
        """
        theString = self._now.strftime("%m")
        return int(theString)

    @property
    def day(self):
        """
        @return 現在 日.
        """
        theString = self._now.strftime("%d")
        return int(theString)
    
    @property
    def hour(self):
        """
        @return 現在 時.
        """
        theString = self._now.strftime("%H")
        return int(theString)
    
    @property
    def min(self):
        """
        @return 現在 分.
        """
        theString = self._now.strftime("%M")
        return int(theString)

    @property
    def sec(self):
        """
        @return 現在 秒.
        """
        theString = self._now.strftime("%S")
        return int(theString)

    def set_time(self):
        """
        @brief  現在時刻を設定.
        @return なし.
        @note   現在時刻をobserverへ更新を通知.
        """
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
