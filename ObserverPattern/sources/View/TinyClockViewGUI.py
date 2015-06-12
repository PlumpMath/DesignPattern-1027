#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
@brief  時計 GUI表示部
        時計本体部から, 通知を受けデータをGUIで表示する.
"""

#PyQt
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

#時計表示部(表示データ保持)
from View.TinyClockView import TinyClockView

class TinyDigitalClockView(QtGui.QWidget):
    """
    @brief  デジタル時計 GUI表示部 クラス.
    @note   以下クラスを継承.
                QtGui.QWidget
    """

    __DEBUG = False

    def __init__(self, parent=None):
        """
        @brief  初期化.
        """
        QtGui.QWidget.__init__(self)
        self.m_DateTimeEdit = None
        self.m_TinyClockView = TinyClockView()

    def setup_ui(self, dateTimeEdit):
        """
        @brief  UIを設定.
        """
        #日付時間ウィジェット.
        self.m_DateTimeEdit = dateTimeEdit
        #QWidgetの親子関係.
        self.setParent(self.m_DateTimeEdit)

    def indicate_redraw(self):
        """
        @brief  デジタル時計を描画.
        """
        #日付を設定.
        theDate = QtCore.QDate(self.m_TinyClockView.year, self.m_TinyClockView.month, self.m_TinyClockView.day)
        self.m_DateTimeEdit.setDate(theDate)

        #時間を設定.
        theTime = QtCore.QTime(self.m_TinyClockView.hour, self.m_TinyClockView.min, self.m_TinyClockView.sec)
        self.m_DateTimeEdit.setTime(theTime)

        #選択を解除.
        self.m_DateTimeEdit.setCurrentSectionIndex(self.m_DateTimeEdit.NoSection)

        if(self.__DEBUG): print("DigitalClock %02d-%02d-%02d %02d:%02d:%02d")%(self.m_TinyClockView.year, self.m_TinyClockView.month, self.m_TinyClockView.day, self.m_TinyClockView.hour, self.m_TinyClockView.min, self.m_TinyClockView.sec)



#アナログ時計 表示部 クラス.
import math
class TinyAnalogClockView(QtGui.QWidget):
    """
    @brief  アナログ時計 GUI表示部 クラス.
    @note   以下クラスを継承.
                QtGui.QWidget
    """

    def __init__(self, parent=None):
        """
        @brief  初期化.
        """
        #スーパークラスを初期化.
        QtGui.QWidget.__init__(self, parent=parent)

        #ウィジェットの幅/高さ.
        self.width = parent.width()
        self.height = parent.height()

        #描画領域.(QtGui.QPixmap)
        self._offscreen = None

        #秒針/短針/長針を描画する為のペン.(QtGui.QPen)
        self._sec_needle_pen = None
        self._min_needle_pen = None
        self._hour_needle_pen = None

        #秒針/短針/長針の長さ.
        self._sec_needle_length = 0
        self._min_needle_length = 0
        self._hour_needle_length = 0

        #日付ウィジェット.
        self.m_DateEdit = None

        self.m_TinyClockView = TinyClockView()

    def setup_ui(self, dateEdit):
        """
        @brief  UIを設定.
        """
        #日付ウィジェット.
        self.m_DateEdit = dateEdit

        #QWidgetの親子関係.
        self.m_DateEdit.setParent(self)

        #時計の針の長さ.
        self._sec_needle_length = 70
        self._min_needle_length = 90
        self._hour_needle_length = 60

        #時計の針の色と太さ.
        self._sec_needle_pen = QtGui.QPen(QtCore.Qt.yellow, 2)
        self._min_needle_pen = QtGui.QPen(QtCore.Qt.green, 3)
        self._hour_needle_pen = QtGui.QPen(QtCore.Qt.red, 6)

        #時計の描画領域.
        self._offscreen = QtGui.QPixmap(self.width, self.height)

    def paintEvent(self, paint_event):
        """
        @brief  再描画（再描画イベントが来た場合に走る）.
        @note   QWidget.paintEventをオーバーライド.
        """
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.drawPixmap(0, 0, self._offscreen)
        painter.end()

    def indicate_redraw(self):
        """
        @brief  アナログ時計を描画.
        """
        #クリア.
        self._draw_clear()
        #長針を描画.
        self._draw_hour_needle(self.m_TinyClockView.hour)
        #短針を描画.
        self._draw_min_needle(self.m_TinyClockView.min)
        #秒針を描画.
        self._draw_sec_needle(self.m_TinyClockView.sec)
        #日付を更新.
        self._draw_date()
        #選択を解除. 
        self.m_DateEdit.setCurrentSectionIndex(self.m_DateEdit.NoSection)

        #再描画指示（再描画イベントを発行）
        self.repaint()

    def _draw_clear(self):
        """
        @brief  描画クリア.
        """
        #黒で塗りつぶす.
        self._offscreen.fill(QtCore.Qt.black)

    def _draw_needle(self, rad, pen, length):
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
        painter.begin(self._offscreen)
        #ペンを設定.
        painter.setPen(pen)
        #時計の針を描画.
        painter.drawLine(origin_x, origin_y, origin_x+point_x, origin_y+point_y)
        painter.end()

    def _draw_sec_needle(self, sec):
        """
        @brief  秒針を描画.
        """
        rad = math.radians(sec*(360/60) -90)
        pen = self._sec_needle_pen
        length = self._sec_needle_length
        self._draw_needle(rad, pen, length)

    def _draw_min_needle(self, min):
        """
        @brief  短針を描画.
        """
        rad = math.radians(min*(360/60) -90)
        pen = self._min_needle_pen
        length = self._min_needle_length
        self._draw_needle(rad, pen, length)
        
    def _draw_hour_needle(self, hour):
        """
        @brief  長針を描画.
        """
        rad = math.radians((hour%12)*(360/12) -90)
        pen = self._hour_needle_pen
        length = self._hour_needle_length
        self._draw_needle(rad, pen, length)
        
    def _draw_date(self):
        """
        @brief  日付を設定.
        """
        theDate = QtCore.QDate(self.m_TinyClockView.year, self.m_TinyClockView.month, self.m_TinyClockView.day)
        self.m_DateEdit.setDate(theDate)

