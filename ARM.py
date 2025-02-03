import time
import keyboard
import tkinter as tk
from threading import Thread
from PIL import ImageGrab
import pytesseract
import pyautogui

# Global state
running = False

# Function to toggle the running state when F12 is pressed
def toggle_running():
    global running
    running = not running
    update_gui_state()

# Function to update GUI state
def update_gui_state():
    if running:
        state_label.config(text="Cycle: ON", fg="green")
    else:
        state_label.config(text="Cycle: OFF", fg="red")

# Function to extract text from a specific region of the screen
def extract_text_from_screen(region):
    screenshot = ImageGrab.grab(bbox=region)
    text = pytesseract.image_to_string(screenshot, config='--psm 6')
    return text.strip()

# Function that performs the automated key presses
def automation_loop():
    last_state_update = time.time()  # Track last state update time
    r_key_held = False  # Flag to track if the R key is held down

    while True:
        if running:
            # Update state every 1 second
            if time.time() - last_state_update > 1:
                update_gui_state()
                last_state_update = time.time()

            # Check for "Restart Mission" text
            region = (1623, 536, 1770, 566)
            detected_text = extract_text_from_screen(region)
            
            if "Restart Mission" in detected_text:
                if not r_key_held:  # Only press R if it's not already held
                    pyautogui.keyDown('r')  # Hold R down
                    r_key_held = True
            else:
                if r_key_held:  # Release R if the text is no longer detected
                    pyautogui.keyUp('r')
                    r_key_held = False

            # Commented out the press 'F' logic ReEnable it if you need it...
            # pyautogui.press('f')
            time.sleep(3)  # Wait for the rest of the cycle

        time.sleep(0.1)  # Prevent excessive CPU usage

# Function to start the automation in a separate thread
def start_automation():
    thread = Thread(target=automation_loop, daemon=True)
    thread.start()

# Create the main window
root = tk.Tk()
root.title("AutoRestartMission")
root.attributes("-topmost", 1)
root.configure(bg="#2e2e2e")

# GUI elements
state_label = tk.Label(root, text="Cycle: OFF", font=("Arial", 16), fg="red", bg="#2e2e2e")
state_label.pack(pady=10)

toggle_button = tk.Button(root, text="Toggle Cycle (F12)", font=("Arial", 14), command=toggle_running, bg="#4f4f4f", fg="white")
toggle_button.pack(pady=10)

# Start the automation thread
start_automation()

# Set up the hotkey for F12 to toggle the state
keyboard.add_hotkey('F12', toggle_running)

# Handle graceful exit
def on_close():
    global running
    running = False
    root.quit()

root.protocol("WM_DELETE_WINDOW", on_close)

# Start the Tkinter event loop
root.mainloop()
