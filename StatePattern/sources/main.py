#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

from State import SkinFactory

class ButtonBoxWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent=parent)
        self.setup_ui()

    def setup_ui(self):
        #ボタンを生成.
        self.start_button = QtGui.QPushButton("START", parent=self)
        self.stop_button = QtGui.QPushButton("STOP", parent=self)
        self.reset_button = QtGui.QPushButton("RESET", parent=self)
        self.quit_button = QtGui.QPushButton("QUIT", parent=self)

        #ボタンを配置.
        layout = QtGui.QGridLayout()
        layout.addWidget(self.start_button, 0,  0)
        layout.addWidget(self.stop_button,  0,  1)
        layout.addWidget(self.reset_button, 1,  0)
        layout.addWidget(self.quit_button,  1,  1)
        self.setLayout(layout)

class CountDownWidget(QtGui.QWidget):
    INTERVAL = 10.0         #10msecのインターバル
    COUNT = 30.0*1000       #30秒(msecで指定)

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent=parent)
        self.lcd_number = QtGui.QLCDNumber(parent=self) #LCDディスプレイ.
        self.timer = QtCore.QTimer(parent=self)         #タイマー.
        self.interval = self.INTERVAL                   #インターバル.
        self.count = self.COUNT                         #カウンター.

        self.setup_ui()

    def setup_ui(self):
        self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)

        #QTimer設定.
        self.timer.setInterval(self.interval)
        self.timer.timeout.connect(self.do_countdown)

        #QLCDNumber設定.
        self.lcd_number.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.lcd_number.setFrameStyle(QtGui.QFrame.NoFrame)
        self.lcd_number.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_number.setDigitCount(6)

        #QLCDNumberを配置.
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.lcd_number)
        self.setLayout(layout)

        self.reset_count()

    def set_skin(self):
        """
        @brief  QLCDNumberの前景色と背景色を設定. 
        @note   ステートパターンを利用して色を取得する.
        """
        theSkinFactory = SkinFactory()
        theSkin = theSkinFactory.create(self.count/self.COUNT)

        #前景色を取得.
        theForeColor = theSkin.fore_color()
        #背景色を取得.
        theBackColor = theSkin.back_color()

        # get the palette
        thePalette = self.lcd_number.palette()
        #前景色を設定.
        thePalette.setColor(thePalette.WindowText, theForeColor)
        #背景色を設定.
        thePalette.setColor(thePalette.Window, theBackColor)
        self.lcd_number.setAutoFillBackground(True)
        # set the palette
        self.lcd_number.setPalette(thePalette)

    def update_display(self):
        """
        @brief  表示をアップデート.
        """
        #スキンを設定.
        self.set_skin()

        #タイマーの数値を設定.
        self.lcd_number.display("%6.2f"%(self.count/1000.0))
        #タイマーを表示.
        self.lcd_number.update()

    def do_countdown(self):
        """
        @brief  タイマーをカウントダウン実行.
        """
        self.count -= self.interval
        self.update_display()
        if self.count <= 0:
            self.stop_countdown()

    def start_countdown(self):
        """
        @brief  タイマーをスタート.
        """
        if self.count > 0:
            self.timer.start()

    def stop_countdown(self):
        """
        @brief  タイマーをストップ.
        """
        self.timer.stop()

    def reset_count(self):
        """
        @brief  タイマーをリセット.
        """
        self.count = self.COUNT
        self.update_display()

def main():
    app = QtGui.QApplication(sys.argv)

    #パネルを生成.
    panel = QtGui.QWidget()

    #タイマー表示部を生成.
    countdown_widget = CountDownWidget(parent=panel)
    #ボタン表示部を生成.
    button_box_widget = ButtonBoxWidget(parent=panel)

    #ボタンと動作を接続.
    button_box_widget.start_button.clicked.connect(countdown_widget.start_countdown)
    button_box_widget.stop_button.clicked.connect(countdown_widget.stop_countdown)
    button_box_widget.reset_button.clicked.connect(countdown_widget.reset_count)
    button_box_widget.quit_button.clicked.connect(app.quit)

    #タイマー表示部とボタン表示部を配置. パネルの上にタイマー表示部とボタン表示部を乗せる.
    panel_layout = QtGui.QVBoxLayout()
    panel_layout.addWidget(countdown_widget)
    panel_layout.addWidget(button_box_widget)
    panel.setLayout(panel_layout)
    panel.setFixedSize(320, 200)

    #メインウィンドウを生成. メインウィンドウの上にパネルを乗せる.
    main_window = QtGui.QMainWindow()
    main_window.setWindowTitle("Timer")
    main_window.setCentralWidget(panel)
    main_window.show()

    app.exec_()

if __name__ == '__main__':
    main()

