# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'faceGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(691, 512)
        self.btnImage = QtWidgets.QPushButton(Form)
        self.btnImage.setGeometry(QtCore.QRect(590, 460, 81, 31))
        self.btnImage.setObjectName("btnImage")
        self.lbl_tempImg = QtWidgets.QLabel(Form)
        self.lbl_tempImg.setGeometry(QtCore.QRect(20, 10, 641, 431))
        self.lbl_tempImg.setText("")
        self.lbl_tempImg.setObjectName("lbl_tempImg")
        self.btnWebcam = QtWidgets.QPushButton(Form)
        self.btnWebcam.setGeometry(QtCore.QRect(20, 460, 81, 31))
        self.btnWebcam.setObjectName("btnWebcam")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Face Recognition"))
        self.btnImage.setText(_translate("Form", "Scan Image"))
        self.btnWebcam.setText(_translate("Form", "Scan Webcam"))
