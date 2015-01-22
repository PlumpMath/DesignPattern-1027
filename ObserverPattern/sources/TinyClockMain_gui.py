#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
@brief  TinyClock GUI版.
        PyQtを使用している.
        TinyClock GUI版を使用するには, PyQtのインストールが必要.
"""

import sys

#PyQt
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

#時計本体部
from Model.TinyClockModel import TinyClockModel

#時計表示部
from View.mainwindow import Ui_MainWindow
from View.TinyClockViewGUI import TinyDigitalClockView
from View.TinyClockViewGUI import TinyAnalogClockView

class ClockViewWidget(QtGui.QMainWindow, Ui_MainWindow):
    """
    @brief  TinyClock GUI版を表示する為のウィジェット.
    """

    def __init__(self, *args, **kw):
        """
        @brief  初期化.
        """
        #スーパークラスの初期化.
        QtGui.QMainWindow.__init__(self, *args, **kw)
        self.setupUi(self)

        #時計本体部を生成.
        self.ClockModel = TinyClockModel()

        #デジタル時計表示部を生成.
        self.DigitalClock = TinyDigitalClockView()
        self.DigitalClock.setup_ui(self.dateTimeEdit)

        #アナログ時計表示部を生成.
        self.AnalogClock = TinyAnalogClockView(self.widget)
        self.AnalogClock.setup_ui(self.dateEdit)

        #時計 本体部 と 表示部（データ保持部） を接続
        self.ClockModel.attach(self.DigitalClock.m_TinyClockView)
        self.ClockModel.attach(self.AnalogClock.m_TinyClockView)

        #タイマーを設定.
        self.timer = QtCore.QTimer(parent=self)
        self.timer.setInterval(1*1000)

        #タイマーを設定（時計本体部と接続. 1000msec毎に時刻を設定）.
        self.timer.timeout.connect(self.ClockModel.set_time)

        #タイマーを設定（デジタル時計時計表示部と接続. 1000msec毎に時刻を表示）.
        self.timer.timeout.connect(self.DigitalClock.indicate_redraw)

        #タイマーを設定（アナログ時計時計表示部と接続. 1000msec毎に時刻を表示）.
        self.timer.timeout.connect(self.AnalogClock.indicate_redraw)

        #タイマースタート.
        self.timer.start()

def main():
    """
    @brief  TinyClock GUI版 main処理.
    """
    app = QtGui.QApplication(sys.argv)

    panel = ClockViewWidget()

    main_window = QtGui.QMainWindow()
    main_window.setGeometry(0, 0, panel.width(), panel.height())
    main_window.setWindowTitle("TinyClock")
    main_window.setCentralWidget(panel)
    main_window.show()

    app.exec_()


if __name__=='__main__':
	main()

