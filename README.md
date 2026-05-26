# InazumaAFK

Automatic bot based on **OCR (screen text recognition)** to automate repetitive actions within the game (Inazuma Eleven Victory Road).  
The bot detects text in specific regions of the screen and responds with clicks or keystrokes based on configurable rules.

The application includes:
- OCR engine using Tesseract  
- Automation using PyAutoGUI  
- Graphical interface built with PySide6  
- Support for automated workflows based on screen detection  

---

## Requirements

### 1. Python
Recommended version: **Python 3.10 or higher**

Check your version:
```bash
python --version
```

---

### 2. Tesseract OCR (REQUIRED)

The bot **will NOT work without Tesseract installed**.

#### Download Tesseract (Windows)
Official repository:  
https://github.com/UB-Mannheim/tesseract/wiki  

Install the Windows version (64-bit).

During installation:
- Check the option **Add Tesseract to PATH**
- Recommended language: English

Default path used in the project:
```txt
C:\Program Files\Tesseract-OCR	esseract.exe
```

If you install it in a different location, you must update the path in the code.

---

### 3. Project Dependencies

Install dependencies with:
```bash
pip install -r requirements.txt
```

---

## Using the Bot (VERY IMPORTANT)

### Run as Administrator
For the bot to properly:
- Read the screen  
- Send keystrokes  
- Perform clicks on the game  

**You must run the program as administrator**, both the `.exe` and the `.py` file if you plan to modify the code.

---

### Opponent Team Configuration

In the graphical interface, there is a field called **Opponent Team**.

You must enter the opponent team name using:
- UPPERCASE letters  
- Comma-separated  
- Only the first 2 or 3 letters of each word  

#### Example

Team:
```
Luz Eterna
```

Valid inputs:
```
LUZ,ETE
LU,ET
```

Recommendation:
- Start with 3 letters  
- If OCR detection fails, try 2  

This is used to detect the opponent team text on screen via OCR.

---

### Steps to Use the Bot Correctly

1. Run the program **as administrator**  
2. Enter the **Opponent Team** in the corresponding field  
3. Open the game  
4. Enter a match with the specified opponent team  
5. Press **Start bot**  
6. Keep the game in the **foreground** (not minimized)  
7. Do not move the game window while the bot is running  

If everything is configured correctly, the bot will work automatically.

---

## Screen Resolution (IMPORTANT)

⚠️ This bot is designed to work **ONLY in 1920x1080 resolution**.

Due to how the game handles resolution changes:
- UI elements shift when the resolution changes  
- Button positions are no longer consistent  

Because of this:
- The bot relies on fixed relative positions  
- Changing resolution WILL break functionality  

### Requirements:

- Set your game resolution to **1920x1080**
- Use fullscreen or borderless window mode  
- Do not change resolution while the bot is running  

---

## Build the Executable

The project can be compiled into a single `.exe` using PyInstaller.

Recommended command (PowerShell, single line):
```powershell
pyinstaller --onefile --windowed --name InazumaAFK --icon assets/icon.ico --add-data "assets/icon.ico;assets" main.py
```

The final executable will be generated at:
```
dist/InazumaAFK.exe
```

---

## Important Notes

- OCR is not perfect, so partial matching is used  
- If detection fails, adjust the keywords  
- Do not run the bot in the background  
- Do not minimize the game  
- Only Spanish language support is currently available for the game  
