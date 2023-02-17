from PyQt5 import QtWidgets, QtGui
from loading_ui import Loading_UI
from chat_ui import Chat_UI
from startup_utils import LoadApp, change_window
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QStackedWidget()
    window.setObjectName("window")
    window.setStyleSheet("#window{\n"
                         "    background-color: rgb(0, 0, 0);\n"
                         "}")
    window.resize(550, 650)
    window.setWindowTitle("Senaya - Virtual Assistant")
    window.setWindowIcon(QtGui.QIcon("images/log.png"))
    loadui = Loading_UI()
    chatui = Chat_UI()
    window.addWidget(loadui)
    window.addWidget(chatui)
    window.show()
    thread = LoadApp()
    thread.start()
    thread.signal.connect(lambda signal: change_window(
        window, chatui, loadui, signal, thread))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
