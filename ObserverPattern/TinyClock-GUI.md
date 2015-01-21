#オブザーバーパターン適用例(TinyClock GUI版)
##概要
* デザインパターンのオブザーバーパターンを時計アプリへの適用例をPythonコードで示す。  
* デジタル時計とアナログ時計を表示するアプリを作成した。  GUIで表示することとする。
* このアプリをTinyClockと呼ぶこととする。  
* TinyClockはMVC(Model-View-Controller)で作成することとする。（実際にはModel-View）  

##UML
クラス図とシーケンス図を以下に示す。  

###クラス図
![TinyuClock(GUI版)クラス図](https://raw.githubusercontent.com/kantoku009/DesignPattern/master/ObserverPattern/UML/img/20_TinyClock_GUI_%E3%82%AF%E3%83%A9%E3%82%B9%E5%9B%B3.png)

###シーケンス図
![TinyClock(GUI版)シーケンス図](https://raw.githubusercontent.com/kantoku009/DesignPattern/master/ObserverPattern/UML/img/21_TinyClock_GUI_%E3%82%B7%E3%83%BC%E3%82%B1%E3%83%B3%E3%82%B9%E5%9B%B3.png)


###TinyClockModel Pythonソースコード（一部抜粋）
* TinyClockModelクラスは、MVCモデルのModel部である。  
* TinyClockModelクラスは、Sujectクラスを継承する。  
* TinyClockModelクラスのset_timeメソッドで以下を行う。  
	- 現在時刻取得  
	- Subjectクラスから継承しているnotifyメソッドを呼ぶ  
* notifyメソッドを呼ぶことによって、登録されている全Observerへ通知を行う。  
* ソースコードの詳細は[TinyClockModel.py](https://github.com/kantoku009/DesignPattern/blob/master/ObserverPattern/sources/Model/TinyClockModel.py)を参照。  

TinyClockModelクラスのソースコード一部抜粋を以下に示す。  

```Python
class TinyClockModel(Subject):
    """
    @brief  時計本体部 クラス.
    @note   Subjectクラスを継承.
            時刻を取得し, 表示部へ通知する.
    """
    
    # （中略） #
    
    def set_time(self):
        """
        @brief  現在時刻を設定.
        @return なし.
        @note   現在時刻をobserverへ更新を通知.
        """
        self._now = datetime.datetime.today()
        self.notify(self) 
```


###TinyClockView Pythonソースコード（一部抜粋）
* TinyClockViewクラスは、MVCモデルのView部である。  
* TinyClockViewクラスは、Observerクラスを継承する。  
* TinyClockViewクラスは、表示データを保持するクラスである。  
* TinyClockViewクラスのupdateメソッドで以下を行う。
	- Subjectクラスからの通知を受け取る  
	- 表示用データの保存メソッドであるset_timeを呼ぶ  
* ソースコードの詳細は[TinyClockView.py](https://github.com/kantoku009/DesignPattern/blob/master/ObserverPattern/sources/View/TinyClockView.py)を参照。  

TinyClockViewクラスのソースコード一部抜粋を以下に示す。  

```Python
class TinyClockView(Observer):
    """
    @brief  時計表示部（表示データ保持）.
    @note   Observerクラスを継承.
    """
    
    # (中略) #
    
    def update(self, modifier=None):
        """
        @brief  Subjectから通知を受け取るメソッド.
        @param  modifier    更新情報.
        @note   Observerクラスのメソッドをオーバーライド.
        """
        self.set_time(modifier)
```

##TinyClockViewGUI Pythonソースコード（一部抜粋）
* TinyDigitalClockViewクラスは、デジタル時計のGUI表示部である。
* TinyDigitalClockViewクラスは、メンバー変数としてTinyClockViewクラスを持つ。  
* TinyDigitalClockViewクラスのdraw_viewメソッドは、デジタル時計を描画する。
* ソースコードの詳細は[TinyClockViewGUI.py](https://github.com/kantoku009/DesignPattern/blob/master/ObserverPattern/sources/View/TinyClockViewGUI.py)を参照。 

```Python
class TinyDigitalClockView(QtGui.QWidget):
    """
    @brief  デジタル時計 GUI表示部 クラス.
    @note   以下クラスを継承.
                TinyClockView
                QtGui.QWidget
    """
    def __init__(self, parent=None):
        """
        @brief  初期化.
        """
        QtGui.QWidget.__init__(self)
        self.m_TinyClockView = TinyClockView()

    def draw_view(self):
        """
        @brief  デジタル時計を描画.
        """
        #時間を設定.
        theTime = QtCore.QTime(self.m_TinyClockView.hour,
         						self.m_TinyClockView.min, 
         						self.m_TinyClockView.sec)
        self.m_DateTimeEdit.setTime(theTime)

    # （中略） #
```

* TinyAnalogClockViewクラスは、アナログ時計のGUI表示部である。
* TinyAnalogClockViewクラスは、メンバー変数としてTinyClockViewクラスを持つ。
* TinyAnalogClockViewクラスのdraw_viewメソッドは、アナログ時計を描画する。
* ソースコードの詳細は[TinyClockViewGUI.py](https://github.com/kantoku009/DesignPattern/blob/master/ObserverPattern/sources/View/TinyClockViewGUI.py)を参照。 

```Python
class TinyAnalogClockView(QtGui.QWidget):
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
        QtGui.QWidget.__init__(self, parent=parent)

        self.m_TinyClockView = TinyClockView()

    def draw_view(self):
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
        
    # （中略） #
```


###TinyClockMain_gui Pythonソースコード
* Subjectクラスのattachメソッドで、時計本体部と表示部を接続している。  
* ソースコードの詳細は[TinyClockMain_gui.py](https://github.com/kantoku009/DesignPattern/blob/master/ObserverPattern/sources/TinyClockMain_gui.py)を参照。

```Python
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
        self.timer.timeout.connect(self.DigitalClock.draw_view)

        #タイマーを設定（アナログ時計時計表示部と接続. 1000msec毎に時刻を表示）.
        self.timer.timeout.connect(self.AnalogClock.draw_view)

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

```

##実行

###実行方法
* 実行方法は、コマンドラインから以下を実行。  
	- $python TinyClockMain_gui.py  

###実行イメージ
* TinyClockMain_guiを実行すると以下のように表示される。  
![TinyClock(GUI版)実行イメージ](https://raw.githubusercontent.com/kantoku009/DesignPattern/master/ObserverPattern/run_image/GUI.png)

##TinyClock(GUI版) Python全ソースコード
以下URLに全ソースコードを保存している。  
[TinyClock(GUI版)](https://github.com/kantoku009/DesignPattern/tree/master/ObserverPattern)

###ディレクトリ構成
ソースコードのディレクトリ構成を以下に示す。  

.  
└── sources						// ソースコードファイルを保存したディレクトリ  
    ├── Lib  
    │   └──  Observer.py		// Observerパターン Pythonソースコード  
    │  
    ├── Model  
    │   ├── Lib -> ../Lib		// シンボリックリンク(１つ上のディレクトリのLib)  
    │   └── TinyClockModel.py	// 時計本体部 Pythonソースコード  
    │  
    ├── View  
    │   ├── GUI					// GUI mainwindow.ui以外使用しない  
    │   │   ├── GUI.pro			// Qt Creatorファイル  
    │   │   ├── GUI.pro.user  
    │   │   ├── main.cpp  
    │   │   ├── mainwindow.cpp  
    │   │   ├── mainwindow.h  
    │   │   └── mainwindow.ui	// GUI メインウィンドウ XML（Qt Creatorで自動生成される）      
    │   │  
    │   ├── Lib -> ../Lib		// シンボリックリンク(１つ上のディレクトリのLib)  
    │   ├── TinyClockView.py	// 時計表示部（データ保持）  
    │   ├── TinyClockViewGUI.py	// 時計表示部（GUI）  
    │   └── mainwindow.py		// mainwindow.uiをPythonソースコードへ変換したもの  
    │   
    └── main_gui.py				// GUI用 main関数（本ファイルをpythonで実行するとデジタル時計とアナログ時計をGUI表示する）   
 
