## Неофициальный ЕЭТК телеграм бот 

Телеграм бот, который уведомляет об изменениях на сайте ЕЭТК

Список основных файлов:
- collect_data_daily.py — Отвечает за парсинг и скачивание ежедневных изменений
- collect_data_weekly.py — Отвечает за парсинг и скачивание еженедельных расписаний для всех курсов
- collect_kitties.py — Отвечает за милых котиков :)
- eetkbot.py — **Исполняемый файл** телеграм бота
- main.py — **Исполняемый файл** отлова любых изменений на сайте

Как уже можно было понять, для корректной работы нужно запускать 2 файла - eetkbot.py и main.py

Однако по одиночке они тоже работают

Внутри каждого файла присутствуют комментарии о том как все работает и для чего это нужно

Поднимать бота можно как на windows, так и на linux. Лично я использовал VDS на ОС ubuntu.

### Инструкция для Linux:
После подключения к VDS вводим в терминал следующее:
```
Установим Python версии не ниже 3.7 (самостоятельно)
sudo apt install python3-venv
```
Загрузим на наш выделенный сервер файлы проекта. Это можно сделать как с помощью различных файловых менеджеров, с помощью которых вы подключились, так и просто клонируя этот репозиторий. Ничего сложного :)

Перейдем в папку с проектом на выделенном сервере и создадим виртуальное окружение
```
cd "имя папки"
python3 -m venv venv
source venv/bin/activate
```
Обновим пакетный менеджер и установим необходимые для работы библиотеки
```
pip install -U pip
pip install lxml requests fake-useragent beautifulsoup4 aiogram google-search-results pydantic
```
Ну вот и всё. Нужные библиотеки установлены. Теперь мы можем запускать бота

Однако чтобы он работал даже без вашего присутствия необходимо запустить его в отдельном экране с помощью утилиты screen. Если она не установлена по умолчанию, то скачать ее можно командой ***apt install screen***

Про использование screen хорошо расписано [здесь](https://wiki.merionet.ru/servernye-resheniya/40/kak-polzovatsya-utilitoj-screen-v-linux/)

Создадим два экрана для двух исполняемых файлов
```
screen -S main
screen -S eetkbot
```
С помощью команды ***screen -r main*** зайдем в экран и запустим в нём исполняемый файл
```
python3.7 main.py
```
Чтобы остановить работу скрипта нажимаем Ctrl+C

Чтобы свернуть экран нажимаем Ctrl+A и D

Аналогичным образом во втором экране запускаем второй исполняемый файл

### Инструкция для Windows:
Установим Python с [официального сайта](https://www.python.org/downloads/) версии не ниже 3.7

При установке обязательно ставим галочку на **Add Python to PATH**

Загрузим файлы проекта и поместим их в одну папку

Открываем cmd или PowerShell Terminal в этой папке и создадим виртуальное окружение
```
python -m venv venv
.\.venv\Scripts\activate
```
Теперь загрузим необходимые библиотеки
```
pip install lxml requests fake-useragent beautifulsoup4 aiogram google-search-results pydantic
```
Для каждого из исполняемых файлов нужно своё окно командной строки. Это значит, что нужно открыть еще одно окно cmd или PowerShell Terminal и активировать в нём виртуальное окружение
```
.\.venv\Scripts\activate
```
Запустим исполняемый файл командой ***python main.py***

Аналогичным образом во втором окне запускаем второй исполняемый файл

## Возможные проблемы при запуске
```
UnicodeEncodeError: 'latin-1' codec can't encode characters in position 0-7: ordinal not in range(256)
```
Такая ошибка означает, что в вашем VDS не установлена RU локализация, которая необходима для работы.

Решение здесь: https://qna.habr.com/q/684410, плюсом к этому нужно прописать в рабочем экране ***LANG=ru_RU.UTF***


