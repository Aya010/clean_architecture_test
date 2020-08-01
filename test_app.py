import sys
from PyQt5.QtWidgets import QApplication
from test.user_cases.test_qt_ui_init import QtInit

app = QApplication(sys.argv)
ex = QtInit()
sys.exit(app.exec_())