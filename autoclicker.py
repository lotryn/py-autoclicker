import pyautogui
import time
import threading
import tkinter as tk

def on_press(key):
    global running
    try:
        if key.char == 'a':
            running = not running
    except AttributeError:
        pass

def autoclick():
    global running
    while True:
        if running:
            pyautogui.click()
            time.sleep(interval.get())

def start_clicking():
    global thread
    thread = threading.Thread(target=autoclick)
    thread.start()

def stop_clicking():
    global running
    running = False
    thread.join()

def on_closing():
    stop_clicking()
    root.destroy()

root = tk.Tk()
root.title("Autoclicker")

# Create a label for the number of clicks
clicks_label = tk.Label(root, text="Number of clicks:")
clicks_label.grid(row=0, column=0)

# Create an entry for the number of clicks
num_clicks = tk.StringVar(value='100')
clicks_entry = tk.Entry(root, textvariable=num_clicks)
clicks_entry.grid(row=0, column=1)

# Create a label for the interval
interval_label = tk.Label(root, text="Interval (seconds):")
interval_label.grid(row=1, column=0)

# Create an entry for the interval
interval = tk.StringVar(value='0.1')
interval_entry = tk.Entry(root, textvariable=interval)
interval_entry.grid(row=1, column=1)

# Create start and stop buttons
start_button = tk.Button(root, text="Start", command=start_clicking)
start_button.grid(row=2, column=0)

stop_button = tk.Button(root, text="Stop", command=stop_clicking)
stop_button.grid(row=2, column=1)

# Create a listener for the 'a' key
listener = pynput.keyboard.Listener(on_press=on_press)
listener.start()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
