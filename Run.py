import sys, os
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from sources.form import Ui_Dialog
from SpeakerPy import Speaker

class App(QtWidgets.QDialog, Ui_Dialog):

    def __init__(self) ->None:
        self.radio_btn_dict_default ={"rate":24000,"name":"aidar","format":"mp3"} # Параметры по умолчанию
        self.path_to_file=os.path.dirname(__file__)
        #Инициализация GUI
        super().__init__()  
        self.setupUi(self)   
        #Значения по умолчанию для radio buttom
        self.rButtonRate1.setChecked(True)
        self.rButtonFormat1.setChecked(True)
        self.rButtonMale.setChecked(True)
        #Обработчики кнопок      
        self.pushButtonListen.clicked.connect(self.repeate_text)
        self.pushButtonSave.clicked.connect(self.save_to_file)
        #Обработка кнопок radio
        self.rButtonRate1.clicked.connect(lambda: self.checked_radio_buttom("rate1")) 
        self.rButtonRate2.clicked.connect(lambda: self.checked_radio_buttom("rate2")) 
        self.rButtonMale.clicked.connect(lambda: self.checked_radio_buttom("male")) 
        self.rButtonFemale.clicked.connect(lambda: self.checked_radio_buttom("female")) 
        self.rButtonFormat1.clicked.connect(lambda: self.checked_radio_buttom("format1")) 
        self.rButtonFormat2.clicked.connect(lambda: self.checked_radio_buttom("format2")) 

    def get_text(self) -> str:
        '''Получить текст из plainTextEdit'''
        if self.plainTextEdit.toPlainText()=="":
            self.send_message_box(text_msg="Текст не обнаружен, введите текст и попробуйте заново.")
            return ""
        else: return "<speak>" + self.plainTextEdit.toPlainText() + "</speak>"

    def send_message_box(self, text_msg: str, icon: str = "Information") -> None:
        '''Вывод сообщения на экран (ошибка, информация, критическая ошибка и тд.)'''
        msg = QMessageBox(self)
        msg.setWindowTitle("ArtPY message")
        msg.setText(text_msg)
        if icon=="Warning":
            msg.setIcon(QMessageBox.Icon.Warning)
        elif icon=="Information":
            msg.setIcon(QMessageBox.Icon.Information)
        elif icon=="Question":
            msg.setIcon(QMessageBox.Icon.Question)
        elif icon=="Critical":
            msg.setIcon(QMessageBox.Icon.Critical)
        msg.exec()

    def repeate_text(self) -> None:
        '''Воспроизвести написанный текст с указанными параметрами'''
        speak = Speaker()
        speak.check_file_model()
        _rate=self.radio_btn_dict_default["rate"]
        _speaker=self.radio_btn_dict_default["name"]
        if self.get_text() != "":
            speak.repeate(rate=_rate,text=self.get_text(),speaker=_speaker)

    def save_to_file(self) -> None:
        '''Сохранение данных в аудио файл с указанными параметрами'''
        speak = Speaker()
        speak.check_file_model()
        _rate=self.radio_btn_dict_default["rate"]
        _format=self.radio_btn_dict_default["format"]
        _speaker=self.radio_btn_dict_default["name"]
        if self.get_text() != "":
            speak.save(rate=_rate,format=_format,text=self.get_text(),speaker=_speaker)
            startfine(self)
            
    
    def checked_radio_buttom(self, r_button_name: str) ->None:
        '''Меняет значения словаря (radio_btn_dict_default) при событии клик у QRadioButtom'''
        if r_button_name == "rate1":
            self.radio_btn_dict_default["rate"]=24000
        if r_button_name == "rate2":
            self.radio_btn_dict_default["rate"]=48000
        if r_button_name == "male":
            self.radio_btn_dict_default["name"]="aidar"
        if r_button_name == "female":
            self.radio_btn_dict_default["name"]="kseniya"
        if r_button_name == "format1":
            self.radio_btn_dict_default["format"]="mp3"
        if r_button_name == "format2":
            self.radio_btn_dict_default["format"]="wav"

def startfine(self) -> None:
    '''Открывает папку с аудио файлами'''
    if os.name == "nt":
        os.startfile(self.path_to_file+r"\out")
    else:
        os.system(f'open {self.path_to_file+r"/out"}')

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = App()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    sys.exit(app.exec())  # и запускаем приложение

if __name__=="__main__":
    main()