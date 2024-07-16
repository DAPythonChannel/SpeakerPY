from SpeakerPy import Speaker
#Импорт Qt libs для формирования GUI и обработчиков событий
from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox

import sys, os
from sources.form import Ui_Dialog

class App(QtWidgets.QDialog, Ui_Dialog):

    def __init__(self) ->None:
        super().__init__()  
        self.setupUi(self)   

        # '''Обработчики кнопок'''      
        # self.pushButtonListen.clicked.connect()
        self.pushButtonSave.clicked.connect(self.get_text)  

    def get_text(self):
        msg = QMessageBox(self)         
        msg.setWindowTitle('title')
        msg.setText('<speak>' + self.plainTextEdit.toPlainText() + '</speak>')
        msg.exec()

        # self.label.setText(_translate("Dialog", "Выберете частоту:"))
        # self.rButtonRate1.setText(_translate("Dialog", "24000"))
        # self.rButtonRate2.setText(_translate("Dialog", "48000"))
        # self.label_2.setText(_translate("Dialog", "Выберете голос:"))
        # self.rButtonMale.setText(_translate("Dialog", "Мужской"))
        # self.rButtonFemale.setText(_translate("Dialog", "Женский"))
        # self.label_3.setText(_translate("Dialog", "Формат сохранения файла:"))
        # self.rButtonFormat1.setText(_translate("Dialog", "mp3"))
        # self.rButtonFormat2.setText(_translate("Dialog", "wav"))
        # self.pushButtonListen.setText(_translate("Dialog", "Прослушать"))
        # self.pushButtonSave.setText(_translate("Dialog", "Сохранить в файл")) 


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = App()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    sys.exit(app.exec())  # и запускаем приложение

# text = """
#     <speak>
#         Внимание!!! 
#         Пожа+рная тревога!!!
#         Тушите ЮЛЮ!
#     </speak>
#     """

if __name__=="__main__":
    main()