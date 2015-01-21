#デザインパターンのオブザーバーパターンのメモ

* オブザーバーパターンを使用すると疎結合なアプリケーションを作成可能。 
　(GUIのアプリケーションでよく使用されている。)
* オブザーバーパターンは、「通知者」から「観測者」に状態を通知する。
* オブザーバーパターンのメリットとしては、観測者は通知を受け取った場合に動作する。
　(ポーリングしなくともよい。)
* 通知者をSubjectクラス、観測者をObserverクラスとする。
* Subjectクラスは、Observerクラスを持つ。
* Subjectクラスは、Observerクラスを複数持ってもよい。この場合、SubjectクラスはすべてのObserverクラスへ通知を行う。

----

##Observerパターンのクラス図
![ObserverPattern クラス図](https://raw.githubusercontent.com/kantoku009/DesignPattern/master/ObserverPattern/UML/img/00_ObserverPattern_%E3%82%AF%E3%83%A9%E3%82%B9%E5%9B%B3.png)

##ObserverクラスのPythonソースコード
* Observerクラスは、Subjectクラスから通知を受け取る。
* 抽象クラスの為、インスタンスは作成しないこと。
* Subjectクラスからの通知は、updateメソッドで受け取る。
* updateメソッドは、継承したクラスでオーバーライドする。
* ソースコードの詳細は[Observer.py](https://github.com/kantoku009/DesignPattern/blob/master/ObserverPattern/sources/Lib/Observer.py)を参照。

```Python
class Observer(object):
    """
    @brief  オブザーバークラス.
            更新があった場合, Subjectから通知を受け取るクラス.
    @note   抽象クラス. インスタンスは作成しないこと.    
    """

    def update(self, modifier=None):
        """
        @brief  Subjetから通知を受け取るメソッド.
        @param  modifier    更新情報.
        @note   本メソッドは継承したクラスでオーバーライドすること.
        """
        raise NotImplementedError
```

##SubjectクラスのPythonソースコード(一部抜粋)
* Subjectクラスは、登録されているObserverクラス全てに通知をする。
* Observerクラスを登録するには、attachメソッドを使用する。
* Observerクラスに通知するには、notifyメソッドを使用する。
* ソースコードの詳細は[Observer.py](https://github.com/kantoku009/DesignPattern/blob/master/ObserverPattern/sources/Lib/Observer.py)を参照。

```Python
class Subject(object):
    """
    @brief  サブジェクトクラス.
            更新があった場合, Observerへ通知するクラス.
    """

    def __init__(self):
        """
        @brief  初期化.
        @param  メンバー変数 self._observerList 登録されたオブザーバーリスト.   
        """
        self._observerList = []

    def attach(self, observer):
        """
        @brief    Observerを登録する.
        @param    observer 登録するオブザーバー.
        @return   なし.
        """
        if not observer in self._observerList:
            self._observerList.append(observer)

    def notify(self, modifier=None):
        """
        @brief  Observerへ更新を通知するメソッド.
        @param  modifier    更新情報.
        """
        for observer in self._observerList:
            if observer != modifier:
                observer.update(self)
```

----

##参考文献
[17．Observer パターン | TECHSCORE(テックスコア)](http://www.techscore.com/tech/DesignPattern/Observer.html/)

