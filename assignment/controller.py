import sys
import random
from PyQt5 import QtWidgets
from src.view import *
from src.controller.view_controller import controller

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form(controller)
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())