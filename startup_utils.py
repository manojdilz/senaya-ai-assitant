from PyQt5 import QtCore, QtWidgets
import requests
import time
import pickle
import json
import os


class LoadApp(QtCore.QThread):
    signal = QtCore.pyqtSignal(bool)

    def __init__(self):
        super().__init__()

    def run(self):
        self.load_app()

    def load_app(self):
        self.signal.emit(True) if self.get_key(
        ) else self.signal.emit(False)

    def get_key(self):
        code = self.get_code()
        if not code[0]:
            return False
        try:
            key = json.loads(requests.post(
                f'https://senaya-api.onrender.com/get_key?code={code[1]}', timeout=5).text)['key']
            os.environ['OPENAI_API_KEY'] = key
            return True
        except requests.exceptions.ConnectionError:
            time.sleep(2)
            return False
        except Exception:
            return False

    def get_code(self):
        try:
            with open('data/CODE.sav', 'rb') as file:
                key = pickle.load(file)
                return (True, key)
        except:
            return (False, None)


def change_window(window, chatui, loadui, signal, thread):

    if signal:
        window.setCurrentWidget(chatui)
        chatui.label.setText("online")
        chatui.label.setToolTip(QtCore.QCoreApplication.translate(
            "Form", "<html><head/><body><p><span style=\" color:#000000;\">You are online</span></p></body></html>"))
    else:
        QtWidgets.QMessageBox.critical(
            window, "No Internet", "Connect to the Internet and restart the App")
        loadui.gif.stop()
        loadui.loading_gif.setVisible(False)
