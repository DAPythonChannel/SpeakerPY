<h1 align="center"># SpeakerPY </h1>
<h1 align="center">Language:RU </h1>
<h2>Вид программы:</h2>
<image src="sources/form.png" alt="View software">
<h2>Описание ПО:</h2>
<p>Программа переводящая текст в голос для голосового оповещения и создания роликов (ГОиЧС, Охраны труда и тд.).
Программа переводит только русский язык, цифры необходимо прописывать прописью, по необходимости знаки удаления
можно ставить знаком "+".</p>

<h2>Выбор технологий:</h2>
<p>python3.9, torch (мощная либа, работает с моделями, можно создавать/использовать/обучать свои модели), torchaudio(сохраняет модели), wget, PyQt6, soundfile.</p>

<h2>Установка и запуск:</h2>
<p>Устанавливаем 
<a href="https://www.python.org/downloads/release/python-3913/">Python 3.9</a> c официального сайта.</p> 

<p>Устанавливаем нужные библиотеки следующей командой:</p>
<p><code>pip install -r req.txt или pip3.9 install -r req.txt</code></p>

<p>Запускаем ПО:</p>
<p><code>python Run.py или python3.9 Run.py</code></p>

<p>Дополнительная информация <a href="https://github.com/alphacep/awesome-russian-speech?tab=readme-ov-file">тут</a>.</p>

<h2>Проблемы требующие решения:</h2>
<ul>
<li>Не воспроизводятся числа (2,3,4), если прописать прописью -> проблем нет.</li>
<li>Требуется ставить ударения, возможно это не доработка 3 версии модели и в 4 версии все ОК.</li>
<li>Windows не работает формат mp3 у torchaudio, потребуется lib -> soundfile для того чтобы выводить звук.</li>
<li>Не работает wget выкидывает ошибку 403, модель для скачивания: https://models.silero.ai/models/tts/ru/v3_1_ru.pt.</li>
</ul>