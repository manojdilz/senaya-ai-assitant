import openai
import speech_recognition as sr
import googletrans
import pyttsx3
import pyaudio
from about_ui import About_UI
from chat_utils import place_question, place_answer
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal, QCoreApplication
from threading import Thread
import webbrowser as wb
import pickle
import os


recognizer = sr.Recognizer()


def text_to_speech(self, text):
    try:
        thread = Speak(self, text)
        thread.start()
    except OSError:
        QMessageBox.critical(
            self, "Error", "Compatibility error occured with your operating system")


def recive_answer(self, answer, use_speech=False):
    if answer[0] == 'error':
        if answer[1] == 'inet':
            self.label.setText(
                QCoreApplication.translate("Form", "offline"))
            self.label.setToolTip(QCoreApplication.translate(
                "Form", "<html><head/><body><p><span style=\" color:#000000;\">You are offline</span></p></body></html>"))

            QMessageBox.critical(
                self, "Error", "Connect to the Internet")
        else:
            QMessageBox.critical(
                self, "Error", str(answer[1]))
    else:
        if self.label.text() == 'offline':
            self.label.setText(
                QCoreApplication.translate("Form", "online"))
            self.label.setToolTip(QCoreApplication.translate(
                "Form", "<html><head/><body><p><span style=\" color:#000000;\">You are online</span></p></body></html>"))
        place_answer(self, answer[1], use_speech)
    self.send_btn.setEnabled(True)
    self.mic_btn.setEnabled(True)


def ask_question(self, question, use_speech=False):
    if (question.lower() == 'who are you') or (question.lower() == 'who are you ?') or (question.lower() == 'what is your name') or (question.lower() == 'what is your name ?'):
        recive_answer(self, ('done', 'I am Osana'), use_speech)
    else:
        thread = AskQuestion(self, question)
        thread.signal.connect(
            lambda answer: recive_answer(self, answer, use_speech))
        thread.start()


def handle_recognized_text(self, text):
    if text[0] == 'error':
        QMessageBox.critical(
            self, "Error", str(text[1]))
        self.mic_btn.setEnabled(True)
        self.send_btn.setEnabled(True)
    else:
        place_question(self, text[1])
        ask_question(self, text[1], use_speech=True)


def receive_voice(self, audio):
    thread = RecognizeAudio(self, audio)
    thread.signal.connect(lambda text: handle_recognized_text(self, text))
    thread.start()


def recognize_speech(self):
    thread = RecordVoice(self)
    thread.signal.connect(lambda audio: receive_voice(self, audio))
    thread.start()


def translate_handler(source, text):
    thread = TranslateHandler(source, text)
    thread.start()


def open_in_browser(text):
    thread = OpenAnBrowser(text)
    thread.start()


def load_about_ui():
    ui = About_UI()
    ui.show()


class AskQuestion(QThread):
    signal = pyqtSignal(tuple)

    def __init__(self, parent, question):
        super().__init__(parent=parent)
        self.question = question

    def run(self):
        if os.environ.get('OPENAI_API_KEY'):
            openai.api_key = os.environ.get('OPENAI_API_KEY')
        self.signal.emit(self.get_answer())

    def get_answer(self):
        try:
            answer = openai.Completion.create(
                engine="text-davinci-003",
                prompt=self.question,
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.5
            )['choices'][0]['text']
            return ('done', answer[2:])
        except openai.error.APIConnectionError as e:
            return ('error', 'inet')
        except Exception as e:
            return ('error', e)


class RecordVoice(QThread):
    signal = pyqtSignal(sr.AudioData)

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.parent = parent

    def run(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1,
                                      rate=44100, input=True, frames_per_buffer=1024)
        frames = []
        running = True
        self.parent.mic_btn.setStyleSheet("#mic_btn{    \n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(0, 0, 0);\n"
                                       "    border:1px solid rgb(255,0,0);\n"
                                       "    border-radius:25px;\n"
                                       "}\n"
                                       "\n"
                                       "#mic_btn:hover{\n"
                                       "    border-color: rgb(255, 0, 0);\n"
                                       "}")
        try:
            while self.parent.is_recording_started and running:
                data = stream.read(1024)
                frames.append(data)
        except:
            running = False
        stream.stop_stream()
        stream.close()
        audio.terminate()
        frames = b''.join(frames)
        self.signal.emit(sr.AudioData(
            frames, sample_rate=44100, sample_width=2))


class RecognizeAudio(QThread):
    signal = pyqtSignal(tuple)

    def __init__(self, parent, audio):
        super().__init__(parent=parent)
        self.audio = audio

    def run(self):
        try:
            text = recognizer.recognize_google(self.audio)
            self.signal.emit(('done', str(text)))
        except Exception as e:
            self.signal.emit(('error', str(e)))


class Speak(Thread):
    def __init__(self, parent, text):
        super().__init__(daemon=True)
        self.parent = parent
        self.text = text
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)

    def run(self):
        try:
            self.engine.say(self.text)
            self.engine.runAndWait()
            self.engine.stop()
        except Exception as e:
            QMessageBox.critical(
                self.parent, "Error", str(e))


class OpenAnBrowser(Thread):
    def __init__(self, text):
        super().__init__(daemon=True)
        self.text = text

    def run(self):
        base_url = "https://www.google.com/search?q="
        query = "+".join(self.text.split())
        wb.open(base_url + query)


class TranslateHandler(Thread):
    def __init__(self, source, text):
        super().__init__(daemon=True)
        self.translator = googletrans.Translator()
        self.source = source
        self.text = text

    def run(self):
        curr_lang = self.get_current_language()
        if curr_lang == 'en':
            translated_text = self.translator.translate(
                self.text, dest='si', src='en').text
            self.source.setText(translated_text)
            curr_obj_name = self.source.objectName()
            self.source.setObjectName(curr_obj_name[:-2]+'si')
        elif curr_lang == 'si':
            translated_text = self.translator.translate(
                self.text, dest='en', src='si').text
            self.source.setText(translated_text)
            curr_obj_name = self.source.objectName()
            self.source.setObjectName(curr_obj_name[:-2]+'en')

    def get_current_language(self):
        return self.source.objectName()[-2:]
