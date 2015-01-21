#オブザーバーパターン適用例(TinyClock Console版)
##概要
* デザインパターンのオブザーバーパターンを時計アプリへの適用例をPythonコードで示す。  
* デジタル時計とアナログ時計を表示するアプリを作成した。  
* このアプリをTinyClockと呼ぶこととする。  
* TinyClockはMVC(Model-View-Controller)で作成することとする。（実際にはModel-View）  

##実行

###実行方法
* 実行方法は、コマンドラインから以下を実行。  
	- $python TinyClockMain_console.py  
* プログラムは無限ループになっているので、C-cで強制終了。  

###実行イメージ
* TinyClockMain_consoleを実行すると以下のように表示される。  
![TinyClock(console版)実行イメージ](https://raw.githubusercontent.com/kantoku009/DesignPattern/master/ObserverPattern/run_image/console.png)

##UML
クラス図とシーケンス図を以下に示す。  

###クラス図
![TinyuClock(console版)クラス図](https://raw.githubusercontent.com/kantoku009/DesignPattern/master/ObserverPattern/UML/img/10_TinyClock_console_%E3%82%AF%E3%83%A9%E3%82%B9%E5%9B%B3.png)

###シーケンス図
![TinyClock(console版)シーケンス図](https://raw.githubusercontent.com/kantoku009/DesignPattern/master/ObserverPattern/UML/img/11_TinyClock_console_%E3%82%B7%E3%83%BC%E3%82%B1%E3%83%B3%E3%82%B9%E5%9B%B3.png)


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


###TinyClockMain_console Pythonソースコード
* TinyClockMain_consoleは、以下クラスをインスタンス化し、制御する。  
	- TinyClockModel  
	- TinyClockView  
* 時計本体部(TinyClockModel)を以下でインスタンス化
	- theModel  = TinyClockModel()  
* アナログ時計及びデジタル時計をインスタンス化している。
	- theAnalogClockView = TinyClockView()  
	- theDigitalClockView = TinyClockView()  
* Subjectクラスのattachメソッドで、時計本体部と表示部を接続している。  
* 時計表示用にスレッドを生成し、各時計独立で表示するようにしている。  
* ソースコードの詳細は[TinyClockMain_console.py](https://github.com/kantoku009/DesignPattern/blob/master/ObserverPattern/sources/TinyClockMain_console.py)を参照。

```Python
def main():
    """
    @brief  TinyClock console版 main処理
    @note   以下を別スレッドを生成して時刻を表示する.
                アナログ時計
                デジタル時計
            スリープを使用してスレッドを切り替えている為, 
            スレッドの同期はとっていない.
    """
    #時計本体部を生成.
    theModel = TinyClockModel()
    #アナログ時計表示部を生成.
    theAnalogClockView = TinyClockView()
    #デジタル時計表示部を生成.
    theDigitalClockView = TinyClockView()

    #時計 本体部と表示部接続.
    theModel.attach(theAnalogClockView)
    theModel.attach(theDigitalClockView)

    #アナログ時計表示部のスレッドを生成.
    theAnalogClockViewThread= threading.Thread(target=refresh_view, name="AnalogClock", args=[theAnalogClockView])
    theAnalogClockViewThread.setDaemon(True)
    theAnalogClockViewThread.start()

    #デジタル時計表示部のスレッドを生成.
    theDigitalClockViewThread = threading.Thread(target=refresh_view, name="DigitalClock", args=[theDigitalClockView])
    theDigitalClockViewThread.setDaemon(True)
    theDigitalClockViewThread.start()

    while 1:
        theModel.set_time()
        #1秒スリープ.
        time.sleep(1.0)
```

##TinyClock(console版) Python全ソースコード
以下URLに全ソースコードを保存している。  
[TinyClock(Console版)](https://github.com/kantoku009/DesignPattern/tree/master/ObserverPattern)

###ディレクトリ構成
ソースコードのディレクトリ構成を以下に示す。  

.  
└── sources							// ソースコードファイルを保存したディレクトリ  
    ├── Lib  
    │   └──  Observer.py			// Observerパターン Pythonソースコード  
    │  
    ├── Model  
    │   ├── Lib -> ../Lib			// シンボリックリンク(１つ上のディレクトリのLib)  
    │   └── TinyClockModel.py		// 時計本体部 Pythonソースコード  
    │  
    ├── View  
    │   │  
    │   ├── Lib -> ../Lib			// シンボリックリンク(１つ上のディレクトリのLib)  
    │   └── TinyClockView.py		// 時計表示部（データ保持）  
    │  
    └── TinyClockMain_console.py	// コンソール用 main関数（本ファイルをpythonで実行するとコンソールに時刻を表示する）  
 
