#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
@brief  時計表示部（表示データ保持部）
        時計本体部から, 通知を受けデータを表示する.
"""

from Lib.Observer import Observer

class TinyClockView(Observer):
    """
    @brief  時計表示部（表示データ保持）.
    @note   Observerクラスを継承.
    """

    def __init__(self):
        """
        @brief  メンバー変数    表示データ 年/月/日/時/分/秒
        """
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
    def year(self):
        """
        @return 現在 年.
        """
        return self._year

    @property
    def month(self):
        """
        @return 現在 月.
        """
        return self._month

    @property
    def day(self):
        """
        @return 現在 日.
        """
        return self._day

    @property
    def hour(self):
        """
        @return 現在 時.
        """
        return self._hour

    @property
    def min(self):
        """
        @return 現在 分.
        """
        return self._min

    @property
    def sec(self):
        """
        @return 現在 秒.
        """
        return self._sec

    def set_time(self, modifier):
        """
        @brief  表示用 現在時刻を設定.
        @return なし.
        """
        self._year = modifier.year
        self._month = modifier.month
        self._day = modifier.day
        self._hour = modifier.hour
        self._min = modifier.min
        self._sec = modifier.sec

    def get_time(self):
        """
        @brief  時刻を取得.
        @return 時刻を文字列で返す.
        """
        return ("%02d-%02d-%02d %02d:%02d:%02d")%(self.year, self.month, self.day, self.hour, self.min, self.sec)


    def update(self, modifier=None):
        """
        @brief  Subjectから通知を受け取るメソッド.
        @param  modifier    更新情報.
        @note   Observerクラスのメソッドをオーバーライド.
        """
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
