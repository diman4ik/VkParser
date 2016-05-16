# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filter.ui'
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
        Dialog.resize(503, 150)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(160, 120, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayoutWidget = QtGui.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 501, 121))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.cityEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.cityEdit.setObjectName(_fromUtf8("cityEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cityEdit)
        self.spinBoxAgeFrom = QtGui.QSpinBox(self.formLayoutWidget)
        self.spinBoxAgeFrom.setMaximum(999)
        self.spinBoxAgeFrom.setObjectName(_fromUtf8("spinBoxAgeFrom"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinBoxAgeFrom)
        self.spinBoxAgeTo = QtGui.QSpinBox(self.formLayoutWidget)
        self.spinBoxAgeTo.setMaximum(999)
        self.spinBoxAgeTo.setObjectName(_fromUtf8("spinBoxAgeTo"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.spinBoxAgeTo)
        self.performerEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.performerEdit.setObjectName(_fromUtf8("performerEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.performerEdit)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Фильтр", None))
        self.label.setText(_translate("Dialog", "Город", None))
        self.label_2.setText(_translate("Dialog", "Возраст от", None))
        self.label_3.setText(_translate("Dialog", "Возраст до", None))
        self.label_4.setText(_translate("Dialog", "Слушает исполнителя", None))

