#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
@brief  時計 GUI表示部
        時計本体部から, 通知を受けデータをGUIで表示する.
"""

#PyQt
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

#GUI
from mainwindow import Ui_MainWindow

#時計表示部(表示データ保持)
from TinyClockView import TinyClockView

class TinyDigitalClockView(TinyClockView, QtGui.QWidget):
    """
    @brief  デジタル時計 GUI表示部 クラス.
    @note   以下クラスを継承.
                TinyClockView
                QtGui.QWidget
    """

    __DEBUG = False

    def __init__(self, parent=None):
        """
        @brief  初期化.
        """
        TinyClockView.__init__(self)
        QtGui.QWidget.__init__(self)
        self.dateTimeEdit = None

    def setup_ui(self, dateTimeEdit):
        """
        @brief  UIを設定.
        """
        #日付時間ウィジェット.
        self.dateTimeEdit = dateTimeEdit
        #QWidgetの親子関係.
        self.setParent(self.dateTimeEdit)

    def update(self, modifier=None):
        """
        @brief  Subjectから通知を受け取るメソッド.
        @param  modifier    更新情報.
        @note   Observerクラスのメソッドをオーバーライド.
        """
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
    """
    @brief  アナログ時計 GUI表示部 クラス.
    @note   以下クラスを継承.
                TinyClockView
                QtGui.QWidget
    """

    def __init__(self, parent=None):
        """
        @brief  初期化.
        """
        #スーパークラスを初期化.
        TinyClockView.__init__(self)
        QtGui.QWidget.__init__(self, parent=parent)

        #ウィジェットの幅/高さ.
        self.width = parent.width()
        self.height = parent.height()

        #描画領域.(QtGui.QPixmap)
        self.offscreen = None

        #日付ウィジェット.
        self.dateEdit = None

        #秒針/短針/長針を描画する為のペン.(QtGui.QPen)
        self.sec_needle_pen = None
        self.min_needle_pen = None
        self.hour_needle_pen = None

        #秒針/短針/長針の長さ.
        self.sec_needle_length = 0
        self.min_needle_length = 0
        self.hour_needle_length = 0


    def setup_ui(self, dateEdit):
        """
        @brief  UIを設定.
        """
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


    def update(self, modifier=None):
        """
        @brief  Subjectから通知を受け取るメソッド.
        @param  modifier    更新情報.
        @note   Observerクラスのメソッドをオーバーライド.
        """
        #時刻を更新.
        TinyClockView.update(self, modifier)

        #時計を描画
        self.draw_display()

        #再描画指示（再描画イベントを発行）
        self.repaint()

        #選択を解除. 
        self.dateEdit.setCurrentSectionIndex(self.dateEdit.NoSection)

    def draw_display(self):
        """
        @brief  アナログ時計を描画.
        """
        #クリア.
        self.draw_clear()
        #長針を描画.
        self.draw_hour_needle(self.hour)
        #短針を描画.
        self.draw_min_needle(self.min)
        #秒針を描画.
        self.draw_sec_needle(self.sec)
        #日付を更新.
        self.draw_date()

    def draw_clear(self):
        """
        @brief  描画クリア.
        """
        #黒で塗りつぶす.
        self.offscreen.fill(QtCore.Qt.black)

    def draw_needle(self, rad, pen, length):
        """
        @brief  時計の針を描画.
        """
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

    def draw_sec_needle(self, sec):
        """
        @brief  秒針を描画.
        """
        rad = math.radians(sec*(360/60) -90)
        pen = self.sec_needle_pen
        length = self.sec_needle_length
        self.draw_needle(rad, pen, length)

    def draw_min_needle(self, min):
        """
        @brief  短針を描画.
        """
        rad = math.radians(min*(360/60) -90)
        pen = self.min_needle_pen
        length = self.min_needle_length
        self.draw_needle(rad, pen, length)
        
    def draw_hour_needle(self, hour):
        """
        @brief  長針を描画.
        """
        rad = math.radians((hour%12)*(360/12) -90)
        pen = self.hour_needle_pen
        length = self.hour_needle_length
        self.draw_needle(rad, pen, length)
        
    def draw_date(self):
        """
        @brief  日付を設定.
        """
        theDate = QtCore.QDate(self.year, self.month, self.day)
        self.dateEdit.setDate(theDate)

    def paintEvent(self, paint_event):
        """
        @brief  再描画（再描画イベントが来た場合に走る.QWidget.paintEventをオーバーライド）.
        """
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.drawPixmap(0, 0, self.offscreen)
        painter.end()

