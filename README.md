
RU: MouseWatch
MouseWatch - это Python скрипт, который отслеживает движение курсора мыши на вашем компьютере и отправляет скриншоты экрана в указанный вами чат Telegram, когда курсор перемещается.

Установка
Убедитесь, что у вас установлен Python 3. Вы можете скачать его здесь.

Клонируйте этот репозиторий на ваш компьютер:

bash
Copy code
git clone https://github.com/your-username/MouseWatch.git
Установите необходимые библиотеки, используя pip:

Copy code
pip install pyautogui telebot mss pillow tkinter
Использование
Запустите скрипт, используя Python:

Copy code
python MouseWatch.py
Введите токен вашего бота Telegram и ID чата, в который будут отправляться скриншоты.

Нажмите "Start Monitoring" для начала мониторинга.

Скрипт будет работать в фоновом режиме, отслеживая движение курсора и отправляя скриншоты в указанный вами чат Telegram каждый раз, когда курсор перемещается.

Примечание
Этот скрипт предназначен только для образовательных целей и не должен использоваться для недобросовестных целей. Используйте его на свой страх и риск.

Лицензия
Этот проект лицензирован под MIT License - подробности смотрите в файле LICENSE.

EN: MouseWatch
MouseWatch is a Python script that monitors mouse movements on your computer and sends screenshots to the Telegram chat you specify when the cursor moves.

Installing
Make sure you have Python 3 installed. You can download it here.

Clone this repository to your computer:

bash
Copy code
git clone https://github.com/your-username/MouseWatch.git
Install the needed libraries using pip:

Copy code
pip install pyautogui telebot mss pillow tkinter
Using
Run the script using Python:

Copy code
python MouseWatch.py
Enter your Telegram bot's token and the chat ID to which screenshots will be sent.

Click "Start Monitoring" to start monitoring.

The script will run in the background, monitoring cursor movement and sending screenshots to the Telegram chat you specify each time the cursor moves.

Note
This script is intended for educational purposes only and should not be used for unscrupulous purposes. Use it at your own risk.

License
This project is licensed under the MIT License - see the LICENSE file for details.
