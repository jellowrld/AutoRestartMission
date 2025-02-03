# AutoRestartMission

To run this Python script, you'll need to install several dependencies. Here’s a list of the required packages:

1. **tkinter**: This is the standard Python library for creating GUIs, so it might already be installed if you are using a standard Python installation. If it’s not installed, you can install it via the package manager for your operating system. 
   
   - On Ubuntu/Debian: `sudo apt-get install python3-tk`
   - On Windows and macOS, tkinter should be included with Python by default.

2. **pytesseract**: This is an OCR (optical character recognition) tool for Python that uses the Tesseract engine.
   - Install it using pip:
     ```
     pip install pytesseract
     ```

   Additionally, you need to install Tesseract itself:
   - On Ubuntu/Debian: `sudo apt-get install tesseract-ocr`
   - On Windows, download the Tesseract installer from [here](https://github.com/tesseract-ocr/tesseract) and follow the installation instructions. Make sure to add the Tesseract binary to your system's PATH.
   - On macOS: `brew install tesseract`

3. **Pillow**: This library is used for image processing, and `ImageGrab.grab()` relies on it.
   - Install it using pip:
     ```
     pip install Pillow
     ```

4. **pyautogui**: This is the library used to automate the keyboard presses.
   - Install it using pip:
     ```
     pip install pyautogui
     ```

5. **keyboard**: This library allows you to listen to keyboard events (such as the F12 key press).
   - Install it using pip:
     ```
     pip install keyboard
     ```
