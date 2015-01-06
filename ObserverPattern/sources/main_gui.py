#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

from View.mainwindow import Ui_MainWindow

from View.TinyClockView import TinyClockView
from Model.TinyClockModel import TinyClockModel

#デジタル時計 表示部 クラス.
class TinyDigitalClockView(TinyClockView, QtGui.QWidget):
    __DEBUG = False

    def __init__(self, parent=None):
        TinyClockView.__init__(self)
        QtGui.QWidget.__init__(self)
        self.dateTimeEdit = None

    def setup_ui(self, dateTimeEdit):
        #日付時間ウィジェット.
        self.dateTimeEdit = dateTimeEdit
        #QWidgetの親子関係.
        self.setParent(self.dateTimeEdit)

    def update(self, modifier=None):
        #時刻を更新.
        TinyClockView.update(self, modifier)

        #日付を設定.
        theDate = QtCore.QDate(self.year, self.month, self.day)
        self.dateTimeEdit.setDate(theDate)

        #時間を設定.
        theTime = QtCore.QTime(self.hour, self.min, self.sec)
        self.dateTimeEdit.setTime(theTime)

        #選択を解除.
        self.dateTimeEdit.setCurrentSectionIndex(self.dateTimeEdit.NoSection)

        if(self.__DEBUG): print("DigitalClock %02d-%02d-%02d %02d:%02d:%02d")%(self.year, self.month, self.day, self.hour, self.min, self.sec)


#アナログ時計 表示部 クラス.
import math
class TinyAnalogClockView(TinyClockView, QtGui.QWidget):

    def __init__(self, parent=None):
        TinyClockView.__init__(self)
        QtGui.QWidget.__init__(self, parent=parent)

        self.dateEdit = None
        self.sec_needle_pen = None
        self.min_needle_pen = None
        self.hour_needle_pen = None

        self.offscreen = None

        self.width = 0
        self.height = 0

        self.sec_needle_length = 0
        self.min_needle_length = 0
        self.hour_needle_length = 0

        self.width = parent.width()
        self.height = parent.height()

    def setup_ui(self, dateEdit):
        #日付ウィジェット.
        self.dateEdit = dateEdit

        #QWidgetの親子関係.
        self.dateEdit.setParent(self)

        #時計の針の長さ.
        self.sec_needle_length = 70
        self.min_needle_length = 90
        self.hour_needle_length = 60

        #時計の針の色と太さ.
        self.sec_needle_pen = QtGui.QPen(QtCore.Qt.yellow, 2)
        self.min_needle_pen = QtGui.QPen(QtCore.Qt.green, 3)
        self.hour_needle_pen = QtGui.QPen(QtCore.Qt.red, 6)
        self.date_pen = QtGui.QPen(QtCore.Qt.gray, 5)

        #時計の描画領域.
        self.offscreen = QtGui.QPixmap(self.width, self.height)


    #モデル(ClockModel)からupdateが来た場合走る.
    def update(self, modifier=None):
        #時刻を更新.
        TinyClockView.update(self, modifier)

        #時計を描画
        self.draw_display()

        #再描画指示（再描画イベントを発行）
        self.repaint()

        #選択を解除. 
        self.dateEdit.setCurrentSectionIndex(self.dateEdit.NoSection)

    #時計を描画.
    def draw_display(self):
        self.draw_clear()
        self.draw_hour_needle(self.hour)
        self.draw_min_needle(self.min)
        self.draw_sec_needle(self.sec)
        self.draw_date()

    #描画クリア.
    def draw_clear(self):
        #黒で塗りつぶす.
        self.offscreen.fill(QtCore.Qt.black)

    #時計の針を描画.
    def draw_needle(self, rad, pen, length):
        #時計の針の座標原点.
        origin_x = self.width/2
        origin_y = self.height/2
        #時計の針の先端.
        point_x = length*math.cos(rad)
        point_y = length*math.sin(rad)

        painter = QtGui.QPainter()
        painter.begin(self.offscreen)
        #ペンを設定.
        painter.setPen(pen)
        #時計の針を描画.
        painter.drawLine(origin_x, origin_y, origin_x+point_x, origin_y+point_y)
        painter.end()

    #秒針を描画.
    def draw_sec_needle(self, sec):
        rad = math.radians(sec*(360/60) -90)
        pen = self.sec_needle_pen
        length = self.sec_needle_length
        self.draw_needle(rad, pen, length)

    #分針を描画.
    def draw_min_needle(self, min):
        rad = math.radians(min*(360/60) -90)
        pen = self.min_needle_pen
        length = self.min_needle_length
        self.draw_needle(rad, pen, length)
        
    #時針を描画.
    def draw_hour_needle(self, hour):
        rad = math.radians((hour%12)*(360/12) -90)
        pen = self.hour_needle_pen
        length = self.hour_needle_length
        self.draw_needle(rad, pen, length)
        
    #日付を描画.    
    def draw_date(self):
        theDate = QtCore.QDate(self.year, self.month, self.day)
        self.dateEdit.setDate(theDate)

    #再描画（再描画イベントが来た場合に走る.QWidget.paintEventをオーバーライド）.
    def paintEvent(self, paint_event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.drawPixmap(0, 0, self.offscreen)
        painter.end()


class ClockViewWidget(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kw):
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

        #時計 本体部 と 表示部 を接続
        self.ClockModel.attach(self.DigitalClock)
        self.ClockModel.attach(self.AnalogClock)

        #タイマーを設定（時計本体部と接続. 1000mse毎に時刻を設定）
        self.timer = QtCore.QTimer(parent=self)
        self.timer.timeout.connect(self.ClockModel.set_time)
        self.timer.setInterval(1*1000)
        self.timer.start()




def main():
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
