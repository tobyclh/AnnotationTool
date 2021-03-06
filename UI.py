# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from freehand import FreeHandSlot

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(884, 541)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 862, 521))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")        
        self.MainView = FreeHandSlot(self.horizontalLayoutWidget)
        self.MainView.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainView.sizePolicy().hasHeightForWidth())
        self.MainView.setSizePolicy(sizePolicy)
        self.MainView.setMinimumSize(QtCore.QSize(512, 512))
        self.MainView.setMaximumSize(QtCore.QSize(512, 512))
        self.MainView.setMouseTracking(False)
        self.MainView.setObjectName("MainView")
        self.horizontalLayout.addWidget(self.MainView)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.eraseButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.eraseButton.setObjectName("eraseButton")
        self.gridLayout.addWidget(self.eraseButton, 4, 0, 1, 2)
        self.erasem = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.erasem.setObjectName("erasem")
        self.gridLayout.addWidget(self.erasem, 4, 3, 1, 1)
        self.graphicsView = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 256))
        self.graphicsView.setMaximumSize(QtCore.QSize(512, 512))
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 7, 0, 1, 4)
        self.zoomOut = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.zoomOut.setObjectName("zoomOut")
        self.gridLayout.addWidget(self.zoomOut, 5, 2, 1, 2)
        self.erasep = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.erasep.setObjectName("erasep")
        self.gridLayout.addWidget(self.erasep, 4, 2, 1, 1)
        self.paintp = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.paintp.setObjectName("paintp")
        self.gridLayout.addWidget(self.paintp, 3, 2, 1, 1)
        self.paintm = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.paintm.setObjectName("paintm")
        self.gridLayout.addWidget(self.paintm, 3, 3, 1, 1)
        self.zoomIn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.zoomIn.setObjectName("zoomIn")
        self.gridLayout.addWidget(self.zoomIn, 5, 0, 1, 2)
        self.paintButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.paintButton.setObjectName("paintButton")
        self.gridLayout.addWidget(self.paintButton, 3, 0, 1, 2)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 0, 1, 4)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.MainView.view.gw = self.graphicsView
        self.MainView.view.setup_gw()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.eraseButton.setText(_translate("Dialog", "Erase"))
        self.zoomOut.setText(_translate("Dialog", "Zoom Out"))
        self.erasep.setText(_translate("Dialog", "+"))
        self.paintp.setText(_translate("Dialog", "+"))
        self.erasem.setText(_translate("Dialog", "-"))
        self.paintm.setText(_translate("Dialog", "-"))
        self.zoomIn.setText(_translate("Dialog", "Zoom In"))
        self.paintButton.setText(_translate("Dialog", "Paint"))
        self.pushButton_5.setText(_translate("Dialog", "Selection"))
