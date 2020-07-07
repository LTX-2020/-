# -*- coding: utf-8 -*-
"""
幻变声浪图形模块
author:杨博远
"""

import sys
from Ins_monitor import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QLabel


class Main_ui(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()  # 界面绘制交给InitUi方法

    def change_widget(self,event):
        if(event.globalPos().x()>=self.mapToGlobal(self.app2.pos()).x()):
            self.app2.setObjectName('select')
            self.app1.setObjectName('function')
            self.setStyleSheet(self.qssstyle)
        else:
            if self.centralWidget()!=self.ins_monitor:
                self.setCentralWidget(self.ins_monitor)
            self.app2.setObjectName('function')
            self.app1.setObjectName('select')
            self.setStyleSheet(self.qssstyle)

    def initUI(self):
        # 载入样式文件
        with open('style.qss', 'r') as f:
            self.qssstyle = f.read()
            self.setStyleSheet(self.qssstyle)
        # 状态栏
        self.statusBar().showMessage('ready')
            # 创建一个菜单栏
            # menubar = self.menuBar()
            # menubar.setStyleSheet("font-size:20px")
            # # 添加菜单
            # new_action = QAction("新建", self)
            # save_action = QAction("保存", self)
            # open_action = QAction("打开", self)
            # fileMenu = menubar.addMenu("文件")
            # fileMenu.addAction(open_action)
            # fileMenu.addSeparator()
            # fileMenu.addAction(new_action)
            # fileMenu.addAction(save_action)
        # 设置窗口的位置和大小
        self.resize(1300,700)
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
            # # 设置背景颜色为奶奶灰
            # palette1 = QtGui.QPalette()
            # palette1.setColor(palette1.Background, QtGui.QColor(205, 205, 205))
            # self.setPalette(palette1)
            # 想法1：工具栏实现乐器选择
            # 设置工具栏
            # toolbar = self.addToolBar('乐器选择')
            # ins1 = QAction("乐器1",self)
            # ins1.triggered.connect(QApplication.quit)
            # toolbar.addAction(ins1)
            # ins2 = QAction("乐器2", self)
            # ins2.triggered.connect(QApplication.quit)
            # toolbar.addAction(ins2)
        
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
        self.app1 = QLabel("演奏")
        self.app1.setObjectName('select')
        self.app1.mousePressEvent=self.change_widget
        self.app2 = QLabel("界面2")
        self.app2.setObjectName('function')
        self.app2.mousePressEvent = self.change_widget
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
            #放屏幕中间
            # screen = QDesktopWidget().screenGeometry()
            # size = self.geometry()
            # self.move(int((screen.width() - size.width()) / 2),
            #           int((screen.height() - size.height()) / 2))
        # 显示窗口
        self.show()




if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    a = Main_ui()
    sys.exit(app.exec_())
