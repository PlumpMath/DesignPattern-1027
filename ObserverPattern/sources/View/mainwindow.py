# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/mainwindow.ui'
#
# Created: Sun Jan  4 12:03:03 2015
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(260, 420)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.widget = QtGui.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(20, 120, 220, 220))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.dateEdit = QtGui.QDateEdit(self.widget)
        self.dateEdit.setGeometry(QtCore.QRect(60, 100, 100, 24))
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setReadOnly(True)
        self.dateEdit.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.centralWidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(20, 40, 220, 24))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.dateTimeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateTimeEdit.setReadOnly(True)
        self.dateTimeEdit.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.dateTimeEdit.setTime(QtCore.QTime(0, 0, 0))
        self.dateTimeEdit.setCurrentSection(QtGui.QDateTimeEdit.YearSection)
        self.dateTimeEdit.setDisplayFormat(_fromUtf8("yyyy/MM/dd HH:mm:ss"))
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.label_DigitalClock = QtGui.QLabel(self.centralWidget)
        self.label_DigitalClock.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label_DigitalClock.setObjectName(_fromUtf8("label_DigitalClock"))
        self.label_AnalogClock = QtGui.QLabel(self.centralWidget)
        self.label_AnalogClock.setGeometry(QtCore.QRect(20, 100, 81, 16))
        self.label_AnalogClock.setObjectName(_fromUtf8("label_AnalogClock"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 260, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_DigitalClock.setText(_translate("MainWindow", "DigitalClock", None))
        self.label_AnalogClock.setText(_translate("MainWindow", "AnalogClock", None))

