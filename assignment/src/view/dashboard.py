# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import time
from .QSwitchControl import SwitchControl
from .QDigitalClock import DigitalClock
import os

class Ui_Form(object):
    def __init__(self, controller=None):
        self.view_controller = controller

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(898, 759)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setStyleSheet("background-color: rgb(159, 191, 200);\n"
"")
        self.lcdHumidity = QtWidgets.QLCDNumber(Form)
        self.lcdHumidity.setGeometry(QtCore.QRect(60, 360, 151, 141))
        self.lcdHumidity.setStyleSheet("color: rgb(3, 200, 3);")
        self.lcdHumidity.setObjectName("lcdHumidity")
        self.lcdLight = QtWidgets.QLCDNumber(Form)
        self.lcdLight.setGeometry(QtCore.QRect(260, 360, 151, 141))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lcdLight.setFont(font)
        self.lcdLight.setStyleSheet("color: rgb(7, 181, 255);")
        self.lcdLight.setObjectName("lcdLight")
        self.switch_light = QtWidgets.QCheckBox(Form)
        self.switch_light.setGeometry(QtCore.QRect(410, 170, 141, 61))
        self.switch_light.setStyleSheet("color: rgb(255, 98, 108);")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.switch_light.setFont(font)
        self.switch_light.clicked.connect(self.toggle_light)
        self.switch_light.setChecked(True)
        self.switch_light.setObjectName("switch_light")
        self.label_logo = QtWidgets.QLabel(Form)
        self.label_logo.setGeometry(QtCore.QRect(710, 620, 181, 131))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),"view/bk.png")))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.label_humidity = QtWidgets.QLabel(Form)
        self.label_humidity.setGeometry(QtCore.QRect(60, 540, 101, 61))
        self.label_humidity.setStyleSheet("color: rgb(11, 39, 200);")
        self.label_humidity.setObjectName("label_humidity")
        self.label_light = QtWidgets.QLabel(Form)
        self.label_light.setGeometry(QtCore.QRect(290, 540, 101, 61))
        self.label_light.setStyleSheet("color: rgb(255, 16, 80);")
        self.label_light.setObjectName("label_light")
        self.label_ai = QtWidgets.QLabel(Form)
        self.label_ai.setGeometry(QtCore.QRect(710, 550, 101, 61))
        self.label_ai.setStyleSheet("color: rgb(200, 5, 184);")
        self.label_ai.setObjectName("label_ai")
        self.label_mask = QtWidgets.QLabel(Form)
        self.label_mask.setGeometry(QtCore.QRect(660, 400, 221, 61))
        self.label_mask.setStyleSheet("color: rgb(200, 200, 7);\n"
"color: rgb(200, 4, 168);")
        self.label_mask.setObjectName("label_mask")
        self.label_intro = QtWidgets.QLabel(Form)
        self.label_intro.setGeometry(QtCore.QRect(280, 30, 251, 61))
        self.label_intro.setStyleSheet("color: rgb(239, 16, 127);")
        self.label_intro.setObjectName("label_intro")
        self.label_light_switch = QtWidgets.QLabel(Form)
        self.label_light_switch.setGeometry(QtCore.QRect(210, 170, 151, 61))
        self.label_light_switch.setStyleSheet("color: rgb(11, 39, 200);")
        self.label_light_switch.setObjectName("label_light_switch")
        self.label_name_switch = QtWidgets.QLabel(Form)
        self.label_name_switch.setGeometry(QtCore.QRect(210, 230, 151, 61))
        self.label_name_switch.setStyleSheet("color: rgb(214, 7, 255);")
        self.label_name_switch.setObjectName("label_name_switch")
        self.switch_name = QtWidgets.QCheckBox(Form)
        self.switch_name.clicked.connect(self.toggle_name)
        self.switch_name.setChecked(True)
        self.switch_name.setGeometry(QtCore.QRect(410, 230, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.switch_name.setFont(font)
        self.switch_name.setStyleSheet("color: rgb(8, 255, 90);")
        self.switch_name.setObjectName("switch_name")
        self.label_logo_switch = QtWidgets.QLabel(Form)
        self.label_logo_switch.setGeometry(QtCore.QRect(210, 280, 151, 61))
        self.label_logo_switch.setStyleSheet("color: rgb(200, 4, 4);")
        self.label_logo_switch.setObjectName("label_logo_switch")
        self.switch_logo = QtWidgets.QCheckBox(Form)
        self.switch_logo.clicked.connect(self.toggle_logo)
        self.switch_logo.setChecked(True)
        self.switch_logo.setGeometry(QtCore.QRect(410, 280, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.switch_logo.setFont(font)
        self.switch_logo.setObjectName("switch_logo")
        self.label_name = QtWidgets.QLabel(Form)
        self.label_name.setGeometry(QtCore.QRect(280, 80, 251, 91))
        self.label_name.setStyleSheet("color: rgb(239, 16, 127);")
        self.label_name.setObjectName("label_name")
        self.lcd_clock = DigitalClock(Form)
        self.lcd_clock.setGeometry(QtCore.QRect(40, 40, 100, 50))
        self.lcd_clock.setObjectName("lcd_clock")
        self.lcdTemp = QtWidgets.QLCDNumber(Form)
        self.lcdTemp.setGeometry(QtCore.QRect(460, 360, 161, 141))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lcdTemp.setFont(font)
        self.lcdTemp.setStyleSheet("color: rgb(235, 255, 10);")
        self.lcdTemp.setObjectName("lcdTemp")
        self.label_temp = QtWidgets.QLabel(Form)
        self.label_temp.setGeometry(QtCore.QRect(490, 540, 101, 61))
        self.label_temp.setStyleSheet("color: rgb(219, 15, 255);")
        self.label_temp.setObjectName("label_temp")
        self.lcdHumidity.raise_()
        self.lcdLight.raise_()
        self.switch_light.raise_()
        self.label_humidity.raise_()
        self.label_light.raise_()
        self.label_ai.raise_()
        self.label_mask.raise_()
        self.label_intro.raise_()
        self.label_light_switch.raise_()
        self.label_logo.raise_()
        self.label_name_switch.raise_()
        self.switch_name.raise_()
        self.label_logo_switch.raise_()
        self.switch_logo.raise_()
        self.label_name.raise_()
        self.lcd_clock.raise_()
        self.lcdTemp.raise_()
        self.label_temp.raise_()
        
        # Thread
        if self.view_controller:
            self.view_controller.signal_light.connect(self.set_light)
            self.view_controller.signal_humidity.connect(self.set_humidity)
            self.view_controller.signal_temp.connect(self.set_temp)
            self.view_controller.signal_ai.connect(self.set_AI)
            self.view_controller.start(1000)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def toggle_light(self):
        if self.switch_light.isChecked():
            self.view_controller.turn_light_on()
        else:
            self.view_controller.turn_light_off()
    def toggle_logo(self):
        directory = os.path.join(os.getcwd(),"view/bk.png") if self.switch_logo.isChecked() else ''
        self.label_logo.setPixmap(QtGui.QPixmap(directory))
    def toggle_name(self):
        name = ['DANG CAO CUONG','PHAM MANH DUNG'] if self.switch_name.isChecked() else ['','']
        self.label_name.setText(QtCore.QCoreApplication.translate("Form", f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">{name[0]}</span></p><p align=\"center\"><span style=\" font-size:14pt;\">{name[1]}</span></p></body></html>"))
    def set_light(self, num_lit:str):
        assert type(num_lit) is str
        self.lcdLight.display(num_lit)
    def set_humidity(self, num_lit:str):
        assert type(num_lit) is str, type(num_lit)
        self.lcdHumidity.display(num_lit)
    def set_temp(self, num_lit:str):
        assert type(num_lit) is str
        self.lcdTemp.display(num_lit)
    def set_AI(self, num):
        assert type(num) is str
        face_mask = 'MASKED FACE' if num == '0' else 'UNMASKED FACE'
        self.label_mask.setText(QtCore.QCoreApplication.translate("Form", f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">{face_mask}</span></p></body></html>"))


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.switch_light.setText(_translate("Form", "Light Toggle"))
        self.label_humidity.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Humidity</span></p></body></html>"))
        self.label_light.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Light</span></p></body></html>"))
        self.label_ai.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">AI</span></p></body></html>"))
        self.label_mask.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">MASKED FACE</span></p></body></html>"))
        self.label_intro.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">IOT ASSIGNMENT</span></p></body></html>"))
        self.label_light_switch.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Light Switch</span></p></body></html>"))
        self.label_name_switch.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Show Name</span></p></body></html>"))
        self.switch_name.setText(_translate("Form", "Name Toggle"))
        self.label_logo_switch.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Show Logo</span></p></body></html>"))
        self.switch_logo.setText(_translate("Form", "Logo Toggle"))
        self.label_name.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">DANG CAO CUONG</span></p><p align=\"center\"><span style=\" font-size:14pt;\">PHAM MANH DUNG</span></p></body></html>"))
        self.label_temp.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Temp</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
