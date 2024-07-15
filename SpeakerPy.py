import os, torch, wget, torchaudio

class Speaker():

    def __init__(self):
        # Настройки модели
        self.LOCAL_FILE = 'sources/v3_1_ru.pt'
        self.URL_FILE_WGET = 'https://models.silero.ai/models/tts/ru/v3_1_ru.pt'
        self.RATE = 24000
        
    def check_file_model(self) -> None:
        '''Проверяем есть файл модели в ресурсе, если нет скачиваем его.'''
        if not os.path.isfile(self.LOCAL_FILE):
            wget.download(self.URL_FILE_WGET, self.LOCAL_FILE)

    def save_to_file(self, text: str = 'Привет дру+г!',speaker: str = 'aidar',tread: int = 4) -> None:
        '''Инициализируем CPU и указываем кол-во потоков (по умолчанию 4). 
        Загружаю файл модели и сохраняю переведенный текст'''
        device = torch.device('cpu')
        torch.set_num_threads(tread)
        model = torch.package.PackageImporter(self.LOCAL_FILE).load_pickle("tts_models", "model")
        audio = model.apply_tts(ssml_text=text,
                            speaker=speaker,
                            sample_rate=self.RATE,
                            put_accent=True,
                            put_yo=True)
        torchaudio.save('out/t1.mp3',src=audio.unsqueeze(0),sample_rate=self.RATE)