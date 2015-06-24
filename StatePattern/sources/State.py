#! /usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class SkinFactory(object):
    """
    @brief  スキンクラスを生成する クラス.
    """
    __DEBUG__ = False

    def __init__(self):
        pass

    def create(self, i_Value):
        """
        @brief  スキンクラスを生成する.
        @params i_Value 状態判定に使用する変数.
        @return Skinオブジェクト.
        @note   状態の判定にはSkinの具象クラスで実施させる.
        """
        theStateList = [NormalSkin(), WarnSkin(), LimitSkin()]
        for theState in theStateList:
            if( theState.is_state(i_Value) ): return theState

        #状態が判別不能ならば, ノーマルスキン.
        return NormalSkin()


class Skin(object):
    """
    @brief  スキン クラス.
    @note   抽象クラス. インスタンス化はしないこと.
    @note   pythonだと必要ないと思われるが, 念のため.
    """
    def __init__(self):
        pass
    def is_state(self, i_Value):
        """
        @brief  状態を判定する.
        @params i_Value 状態判定に使用する変数.
        @return True:該当状態 / False:該当状態ではない.
        @note   具象クラスで定義すること.
        """
        pass
    def fore_color(self):
        """
        @brief  前景色を取得.
        @params なし.
        @return 前景色. QtColor
        @note   具象クラスで定義すること.
        """
        pass

    def back_color(self):
        """
        @brief  背景色を取得.
        @params なし.
        @return 背景色. QtColor
        @note   具象クラスで定義すること.
        """
        pass

class NormalSkin(Skin):
    """
    @brief    通常スキン クラス.
    """
    def __init__(self):
        Skin.__init__(self)
    def __str__(self):
        return "NormalSkin"
    def __repr__(self):
        return "<NormalSkin>"
    def is_state(self, i_Value):
        """
        @brief  通常スキンか否かを判定する.
        @params i_Value 通常スキンか否かを判定する変数.
        @return True:通常スキン / False:通常スキンではない.
        """
        if( i_Value >= 0.5 ): return True
        else: return False
    def fore_color(self):
        """
        @brief  前景色を取得.
        @params なし.
        @return 前景色. QtColor.
        """
        theColor = Qt.black
        return (theColor)
    def back_color(self):
        """
        @brief  背景色を取得.
        @params なし.
        @return 背景色. QtColor.
        """
        theColor = QColor(237, 237, 237)    #薄い灰色.
        return (theColor)

class WarnSkin(Skin):
    """
    @brief    警告スキン クラス.
    """
    def __init__(self):
        Skin.__init__(self)
    def __str__(self):
        return "WarnSkin"
    def __repr__(self):
        return "<WarnSkin>"
    def is_state(self, i_Value):
        """
        @brief  警告スキンか否かを判定する.
        @params i_Value 警告スキンか否かを判定する変数.
        @return True:警告スキン / False:警告スキンではない.
        """
        if( (0.5>i_Value) and (0.2<=i_Value) ): return True
        else: False
    def fore_color(self):
        """
        @brief  前景色を取得.
        @params なし. 
        @return 前景色. QtColor.
        """
        theColor = Qt.black
        return (theColor)
    def back_color(self):
        """
        @brief  背景色を取得.
        @params なし.
        @return 背景色. QtColor.
        """
        theColor = Qt.yellow
        return (theColor)

class LimitSkin(Skin):
    """
    @brief    リミットスキン クラス.
    """
    def __init__(self):
        Skin.__init__(self)
    def __str__(self):
        return "LimitSkin"
    def __repr__(self):
        return "<LimitSkin>"
    def is_state(self, i_Value):
        """
        @brief  リミットスキンか否かを判定する.
        @params i_Value リミットスキンか否かを判定する変数.
        @return True:リミットスキン / False:リミットスキンではない.
        """
        if( 0.2 > i_Value ): return True
        else: False
    def fore_color(self):
        """
        @brief  前景色を取得.
        @params なし. 
        @return 前景色. QtColor.
        """
        theColor = QColor(245, 245, 245)    #whitesmoke
        return (theColor)
    def back_color(self):
        """
        @brief  背景色を取得.
        @params なし.
        @return 背景色. QtColor.
        """
        theColor = Qt.red
        return (theColor)


