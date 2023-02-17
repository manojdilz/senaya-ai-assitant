from PyQt5 import QtWidgets, QtGui, QtCore
from threading import Thread
import pyttsx3


def place_question(self, question=None):
    if question is not None:
        frame = QtWidgets.QFrame(self.chat_area_content)
        frame.setMinimumSize(QtCore.QSize(210, 50))
        frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame.setFrameShadow(QtWidgets.QFrame.Raised)
        frame.setObjectName(f"frame_{self.frame_index}")
        verticalLayout = QtWidgets.QVBoxLayout(frame)
        verticalLayout.setObjectName("verticalLayout_3")
        label = QtWidgets.QLabel(frame)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        label.setFont(font)
        label.setStyleSheet("")
        label.setWordWrap(True)
        label.setObjectName(f"label_{self.label_index}_en")
        label.setText(question)
        label.installEventFilter(self)
        verticalLayout.addWidget(label)
        self.gridLayout_3.removeItem(self.chat_spacer_1)
        self.gridLayout_3.removeItem(self.chat_spacer_2)
        self.gridLayout_3.addWidget(frame, self.row_index, 1, 1, 1)
        self.row_index += 1
        self.chat_spacer_1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(self.chat_spacer_1, self.row_index, 0, 1, 1)
        self.chat_spacer_2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(self.chat_spacer_2, self.row_index, 1, 1, 1)
        self.row_index += 1
        self.frame_index += 1
        self.label_index += 1
        return

    frame = QtWidgets.QFrame(self.chat_area_content)
    frame.setMinimumSize(QtCore.QSize(210, 50))
    frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
    frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame.setFrameShadow(QtWidgets.QFrame.Raised)
    frame.setObjectName(f"frame_{self.frame_index}")
    verticalLayout = QtWidgets.QVBoxLayout(frame)
    verticalLayout.setObjectName("verticalLayout_3")
    label = QtWidgets.QLabel(frame)
    font = QtGui.QFont()
    font.setFamily("DejaVu Sans")
    font.setPointSize(11)
    label.setFont(font)
    label.setStyleSheet("")
    label.setWordWrap(True)
    label.setObjectName(f"label_{self.label_index}_en")
    label.setText(self.user_input.toPlainText())
    label.installEventFilter(self)
    verticalLayout.addWidget(label)
    self.gridLayout_3.removeItem(self.chat_spacer_1)
    self.gridLayout_3.removeItem(self.chat_spacer_2)
    self.gridLayout_3.addWidget(frame, self.row_index, 1, 1, 1)
    self.row_index += 1
    self.chat_spacer_1 = QtWidgets.QSpacerItem(
        20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    self.gridLayout_3.addItem(self.chat_spacer_1, self.row_index, 0, 1, 1)
    self.chat_spacer_2 = QtWidgets.QSpacerItem(
        20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    self.gridLayout_3.addItem(self.chat_spacer_2, self.row_index, 1, 1, 1)
    self.row_index += 1
    self.frame_index += 1
    self.label_index += 1
    self.user_input.setText("")


def place_answer(self, answer, use_speech=False):
    frame_2 = QtWidgets.QFrame(self.chat_area_content)
    frame_2.setMinimumSize(QtCore.QSize(210, 50))
    frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
    frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_2.setObjectName(f"frame_{self.frame_index}")
    verticalLayout = QtWidgets.QVBoxLayout(frame_2)
    verticalLayout.setObjectName("verticalLayout_4")
    label_2 = QtWidgets.QLabel(frame_2)
    font = QtGui.QFont()
    font.setFamily("DejaVu Sans")
    font.setPointSize(11)
    label_2.setFont(font)
    label_2.setStyleSheet("")
    label_2.setWordWrap(True)
    label_2.setObjectName(f"label_{self.label_index}_en")
    label_2.setText(answer)
    label_2.installEventFilter(self)
    verticalLayout.addWidget(label_2)
    self.gridLayout_3.removeItem(self.chat_spacer_1)
    self.gridLayout_3.removeItem(self.chat_spacer_2)
    self.gridLayout_3.addWidget(frame_2, self.row_index, 0, 1, 1)
    self.row_index += 1
    self.chat_spacer_1 = QtWidgets.QSpacerItem(
        20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    self.gridLayout_3.addItem(self.chat_spacer_1, self.row_index, 0, 1, 1)
    self.chat_spacer_2 = QtWidgets.QSpacerItem(
        20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    self.gridLayout_3.addItem(self.chat_spacer_2, self.row_index, 1, 1, 1)
    self.row_index += 1
    self.frame_index += 1
    self.label_index += 1
    if use_speech:
        tell = TellAnswer(answer)
        tell.start()


class TellAnswer(Thread):
    def __init__(self, answer):
        super().__init__(daemon=True)
        self.answer = answer
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)

    def run(self):
        self.engine.say(self.answer)
        self.engine.runAndWait()
        self.engine.stop()
