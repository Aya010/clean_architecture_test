
import sys
from PyQt5.QtWidgets import QApplication
from user_cases.qt_ui_init import QtInit

app = QApplication(sys.argv)
ex = QtInit()
sys.exit(app.exec_())