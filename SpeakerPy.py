import os, torch, wget, torchaudio, requests, shutil, sounddevice as sd
from datetime import datetime

LOCAL_FILE = os.path.join(os.path.dirname(__file__),"sources","v3_1_ru.pt")
URL_FILE_WGET = "https://models.silero.ai/models/tts/ru/v3_1_ru.pt"
LOCAL_FILE_OUT = os.path.join(os.path.dirname(__file__),"out")

class Speaker():

    def __init__(self):
        '''Настройки модели'''
        
        self.device = torch.device("cpu")
        torch.set_num_threads(4)
        
    def check_file_model(self) -> None:
        '''Проверяем есть файл модели в ресурсе, если нет скачиваем его.'''
        if not os.path.isfile(LOCAL_FILE):
            self.download_model()

    def download_model(self):
        '''Скачивает модель и записывает в файл'''
        r = requests.get(URL_FILE_WGET, stream=True)
        if r.status_code == 200:
            with open(LOCAL_FILE, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

    def save(self, rate: int, format: str, text: str, speaker: str) -> None:
        '''Сохраняет текст в файл выбранного формата (mp3,wav): где rate - это частота, format - формат сохранения файла,
         text - передаваемый текст, speaker -  выбор спикера мужчина или женщина.
         На выходе файл имеет формат sound_data_time.mp3'''
        time = datetime.now().strftime("%d.%m.%Y_%H_%M_%S")
        file_path = os.path.join(LOCAL_FILE_OUT, f"sound_{time}.{format}")

        model = torch.package.PackageImporter(LOCAL_FILE).load_pickle("tts_models", "model") # Загрузка модели
        audio = model.apply_tts(ssml_text=text,
                            speaker=speaker,
                            sample_rate=rate,
                            put_accent=True,
                            put_yo=True) 
        torchaudio.save(file_path,src=audio.unsqueeze(0),sample_rate=rate) 

    def repeate(self, rate: int, text: str, speaker: str = "aidar") -> None:
        '''Воспроизводит введеный текст: где rate - это частота,
         text - передаваемый текст, speaker -  выбор спикера мужчина или женщина'''
        model = torch.package.PackageImporter(LOCAL_FILE).load_pickle("tts_models", "model")
        audio = model.apply_tts(ssml_text=text,
                            speaker=speaker,
                            sample_rate=rate,
                            put_accent=True,
                            put_yo=True)
        sd.play(audio,rate)