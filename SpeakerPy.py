import os, torch, wget, torchaudio
from datetime import datetime

class Speaker():

    def __init__(self):
        '''Настройки модели'''
        self.LOCAL_FILE = "sources/v3_1_ru.pt"
        self.URL_FILE_WGET = "https://models.silero.ai/models/tts/ru/v3_1_ru.pt"
        
    def check_file_model(self) -> None:
        '''Проверяем есть файл модели в ресурсе, если нет скачиваем его.'''
        if not os.path.isfile(self.LOCAL_FILE):
            wget.download(self.URL_FILE_WGET, self.LOCAL_FILE)

    def save(self, rate: int, format: str, text: str, speaker: str = "aidar") -> None:
        '''Инициализируем CPU и указываем кол-во потоков (по умолчанию 4). 
        Загружаю файл модели и сохраняю переведенный текст'''
        time = datetime.now().strftime("%d.%m.%Y_%H_%M_%S")
        file_path = f"out/sound_{time}.{format}"
        device = torch.device("cpu")
        torch.set_num_threads(4)
        model = torch.package.PackageImporter(self.LOCAL_FILE).load_pickle("tts_models", "model")
        audio = model.apply_tts(ssml_text=text,
                            speaker=speaker,
                            sample_rate=rate,
                            put_accent=True,
                            put_yo=True)
        torchaudio.save(file_path,src=audio.unsqueeze(0),sample_rate=rate)

    def repeate(self, rate: int, format: str, text: str, speaker: str = "aidar") -> None:
        pass