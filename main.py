import time
import pyautogui
import telebot
from mss import mss
from PIL import Image
from tkinter import Tk, Label, Entry, Button, StringVar

# Initializing the initial position of the cursor
x, y = pyautogui.position()

# Initializing an object for a screenshot
sct = mss()

def start_monitoring():
    global bot, x, y 
    TOKEN = token_entry.get()
    CHAT_ID = chat_id_entry.get()
    bot = telebot.TeleBot(TOKEN)

    while True:
        # Checking for cursor movement
        if pyautogui.position() != (x, y):
            # Screenshot
            screenshot = sct.grab(sct.monitors[0])
            img = Image.frombytes('RGB', screenshot.size, screenshot.bgra, 'raw', 'BGRX')
            img.save('screenshot.png')

            # Sending a screenshot to Telegram
            with open('screenshot.png', 'rb') as photo:
                bot.send_photo(CHAT_ID, photo)

            # Updating the cursor position
            x, y = pyautogui.position()

        time.sleep(5)  # Pause in 5 seconds

# Creating a window
root = Tk()
root.title("MouseWatch")

# Creating input fields
token_label = Label(root, text="Enter your bot token:")
token_entry = Entry(root)
chat_id_label = Label(root, text="Enter your chat ID:")
chat_id_entry = Entry(root)

# Creating a button to start monitoring
start_button = Button(root, text="Start Monitoring", command=start_monitoring)

# Placement of elements on the window
token_label.pack()
token_entry.pack()
chat_id_label.pack()
chat_id_entry.pack()
start_button.pack()

# Running the window
root.mainloop()
