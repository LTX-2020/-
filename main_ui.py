# -*- coding: utf-8 -*-
"""
幻变声浪图形模块
author:杨博远

当前进度：
乐器模拟(实现中)
乐器转换(?)
"""

import sys
from Ins_monitor import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QLabel, QDesktopWidget


class Main_ui(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()  # 界面绘制交给InitUi方法

    def change_widget(self):
        sender=self.sender()
        if(sender.text()=='界面2'):
            pass
        else:
            if self.centralWidget()!=self.ins_monitor:
                self.setCentralWidget(self.ins_monitor)

    def initUI(self):
        # 载入样式文件
        with open('style.qss', 'r') as f:
            self.qssstyle = f.read()
            self.setStyleSheet(self.qssstyle)
        # 状态栏
        self.statusBar().showMessage('ready')
        # 设置窗口的位置和大小
        self.resize(1400,700)
        # 设置标题栏
        self.setWindowTitle('幻变声浪')
        # self.setWindowFlags(Qt.WindowCloseButtonHint)
        # 设置窗口的图标
        self.setWindowIcon(QIcon('./photos/logo.png'))
        # 设置背景图片
        bg=QPixmap("./photos/bg1.jpg")
        bg=bg.scaled(self.width(),self.height())
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(bg))
        self.setPalette(palette)

        
        # 自定义菜单栏
        # logo图标
        logo = QLabel(self)
        logomap = QPixmap("./photos/logo.png")
        logo.setPixmap(logomap)
        # 名字
        appname = QLabel("name")
        appnamemap=QPixmap("./photos/title.png")
        appnamemap=appnamemap.scaled(QSize(200,50))
        appname.setPixmap(appnamemap)
        # 功能
        self.app1 = QPushButton("演奏")
        self.app1.setObjectName('app')
        self.app1.setCheckable(True)
        self.app1.setChecked(True)
        self.app1.setAutoExclusive(True)
        self.app1.clicked.connect(self.change_widget)
        self.app2 = QPushButton("界面2")
        self.app2.setObjectName('app')
        self.app2.setCheckable(True)
        self.app2.setAutoExclusive(True)
        self.app2.clicked.connect(self.change_widget)
        # 设置按钮
        set_btn = QPushButton(self)
        set_btn.setObjectName('set_btn')
        # 工具栏水平布局
        hbox1 = QHBoxLayout()
        hbox1.setAlignment(Qt.AlignLeft)
        hbox1.addWidget(logo)
        hbox1.addSpacing(60)
        hbox1.addWidget(appname)
        hbox1.addSpacing(60)
        hbox1.addWidget(self.app1)
        hbox1.addStretch()
        hbox1.addWidget(self.app2)
        hbox1.addStretch()
        hbox1.addWidget(set_btn)
        # 用来改背景色的控件
        mtitle = QWidget()
        mtitle.setLayout(hbox1)
        mtitle.setStyleSheet('background-color: rgb(75, 75, 75)')
        #实例化界面
        self.ins_monitor=Ins_monitor()
        self.setMenuWidget(mtitle)
        self.setCentralWidget(self.ins_monitor)
        # 显示窗口
        self.show()


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    a = Main_ui()
    sys.exit(app.exec_())
