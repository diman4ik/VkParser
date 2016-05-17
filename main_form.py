# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vk_parser.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1092, 790)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1091, 791))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.listPeople = QtGui.QListView(self.tab)
        self.listPeople.setGeometry(QtCore.QRect(10, 40, 501, 711))
        self.listPeople.setObjectName(_fromUtf8("listPeople"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 62, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.listMusic = QtGui.QListView(self.tab)
        self.listMusic.setGeometry(QtCore.QRect(530, 40, 551, 711))
        self.listMusic.setObjectName(_fromUtf8("listMusic"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(530, 10, 62, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.peopleFilterButton = QtGui.QPushButton(self.tab)
        self.peopleFilterButton.setGeometry(QtCore.QRect(420, 0, 91, 31))
        self.peopleFilterButton.setObjectName(_fromUtf8("peopleFilterButton"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "VK Parser", None))
        self.label.setText(_translate("Dialog", "Люди", None))
        self.label_2.setText(_translate("Dialog", "Песни", None))
        self.peopleFilterButton.setText(_translate("Dialog", "Обновить", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Музыка", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Статистика", None))

